import random
import subprocess
import sqlite3
import hashlib

from aiogram import types, Router

from src.services.db_functions import check_word, word_extra


check_msg_router = Router()


@check_msg_router.message()
async def check_msg(msg: types.Message, bot):
    word = await check_word(msg.from_user.first_name, msg.text.lower())

    if word:
        extra = await word_extra(msg.from_user.first_name, word.id)
        await bot.send_message(msg.from_user.id, f"{msg.text}")
    else:
        await bot.send_message(msg.from_user.id, "I dont know that word :(")



# def synthesize_ogg(text, model_path, sample_rate=22050):
#     text_hash = hashlib.sha256(f"{text}:{model_path}".encode()).hexdigest()

#     cur = conn.execute("SELECT ogg_data FROM audio WHERE text_hash = ?", (text_hash,))
#     row = cur.fetchone()
#     if row:
#         return row[0]

#     # 1. Piper -> raw PCM
#     piper_result = subprocess.run(
#         ["piper", "--model", model_path, "--output-raw"],
#         input=text.encode("utf-8"),
#         capture_output=True,
#         check=True
#     )
#     raw_pcm = piper_result.stdout

#     # 2. raw PCM -> OGG/Opus через ffmpeg
#     ffmpeg_result = subprocess.run(
#         [
#             "ffmpeg",
#             "-f", "s16le",           # формат входа: raw PCM, 16-bit little-endian
#             "-ar", str(sample_rate),  # частота дискретизации (та же, что у piper)
#             "-ac", "1",                # моно
#             "-i", "pipe:0",            # вход из stdin
#             "-c:a", "libopus",         # кодек Opus (обязателен для Telegram voice)
#             "-b:a", "32k",             # битрейт, достаточно для голоса
#             "-f", "ogg",                # контейнер OGG
#             "pipe:1"                    # вывод в stdout
#         ],
#         input=raw_pcm,
#         capture_output=True,
#         check=True
#     )
#     ogg_bytes = ffmpeg_result.stdout

#     conn.execute(
#         "INSERT INTO audio (text_hash, text, model, ogg_data) VALUES (?, ?, ?, ?)",
#         (text_hash, text, model_path, ogg_bytes)
#     )
#     conn.commit()
#     return ogg_bytes


#     from aiogram.types import BufferedInputFile

#     voice_file = BufferedInputFile(ogg_bytes, filename="voice.ogg")
#     await bot.send_voice(chat_id=chat_id, voice=voice_file)