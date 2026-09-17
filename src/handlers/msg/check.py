import subprocess
from aiogram import types, Router
from aiogram.types import BufferedInputFile

from src.services.db_functions import check_word, word_extra, save_ogg

check_msg_router = Router()

PIPER_PATH = "/home/nami/apps/piper/piper"
MODELS = {
    "en": "/home/nami/apps/piper/models/en_US-lessac-medium.onnx",
    "ru": "/home/nami/apps/piper/models/ru_RU-irina-medium.onnx",
}


def detect_lang(text: str) -> str:
    """Detect language by characters — ru or en."""
    ru_chars = sum(1 for c in text if '\u0400' <= c <= '\u04FF')
    return "ru" if ru_chars > len(text) / 2 else "en"


def synthesize_ogg(text: str, lang: str) -> bytes:
    model_path = MODELS[lang]

    piper = subprocess.run(
        [PIPER_PATH, "--model", model_path, "--output-raw"],
        input=text.encode("utf-8"),
        capture_output=True,
        check=True
    )

    ffmpeg = subprocess.run(
        [
            "ffmpeg",
            "-f", "s16le",
            "-ar", "22050",
            "-ac", "1",
            "-i", "pipe:0",
            "-c:a", "libopus",
            "-b:a", "32k",
            "-f", "ogg",
            "pipe:1"
        ],
        input=piper.stdout,
        capture_output=True,
        check=True
    )
    return ffmpeg.stdout


@check_msg_router.message()
async def check_msg(msg: types.Message, bot):
    word = await check_word(msg.from_user.first_name, msg.text.lower())

    if not word:
        await bot.send_message(msg.from_user.id, "I don't know that word :(")
        return

    word = word[0]  # check_word возвращает список

    # Текстовая инфа
    text = f"<b>{word.eng}</b> — {word.rus}"
    if word.example:
        text += f"\n\n<i>{word.example}</i>"
    await bot.send_message(msg.from_user.id, text, parse_mode="HTML")

    # Аудио
    extra = await word_extra(word.id)
    if extra and extra.ogg_data:
        ogg_bytes = extra.ogg_data
    else:
        # Синтезируем и сохраняем
        lang = detect_lang(word.eng)
        ogg_bytes = synthesize_ogg(word.eng, lang)
        await save_ogg(word.id, ogg_bytes)

    await bot.send_voice(
        chat_id=msg.from_user.id,
        voice=BufferedInputFile(ogg_bytes, filename="voice.ogg")
    )

    # Видео если есть
    if extra and extra.videos:
        for video in extra.videos:
            caption = video.sub if video.sub else None
            await bot.send_video(
                chat_id=msg.from_user.id,
                video=BufferedInputFile(video.data, filename="video.mp4"),
                caption=caption
            )