# add_video.py — запускать руками когда нашёл видео
import asyncio
import sys
from src.services.db_functions import check_word, add_video
from src.config import DB_PATH
import aiosqlite


async def main():
    # Показать word_id по слову
    word = input("Enter word (eng): ").strip().lower()
    
    async with aiosqlite.connect(DB_PATH) as conn:
        async with conn.execute(
            "SELECT id, eng, rus FROM words WHERE eng = ?", (word,)
        ) as cur:
            row = await cur.fetchone()
    
    if not row:
        print(f"Word '{word}' not found in database")
        return
    
    word_id, eng, rus = row
    print(f"Found: [{word_id}] {eng} — {rus}")
    
    video_path = input("Video file path: ").strip()
    sub = input("Subtitles (press Enter to skip): ").strip() or None
    
    await add_video(word_id, video_path, sub)
    print(f"Video added for word '{eng}'")


asyncio.run(main())