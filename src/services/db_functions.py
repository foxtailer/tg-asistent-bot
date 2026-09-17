import random
import aiosqlite
from datetime import datetime
from typing import List, Tuple
from collections import defaultdict, namedtuple

from src.config import DB_PATH

WordRow = namedtuple("WordRow", ["id", "eng", "rus", "example", "day", "lvl"])
ExtraRow = namedtuple("ExtraRow", ["ogg_data", "videos"])  # videos = list of VideoRow
VideoRow = namedtuple("VideoRow", ["id", "data", "sub"])


async def init_db(db_path: str = DB_PATH) -> None:
    async with aiosqlite.connect(db_path) as conn:
        await conn.executescript("""
            CREATE TABLE IF NOT EXISTS users (
                id   INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE,
                bot  TEXT DEFAULT 'ENG' CHECK (LENGTH(bot) = 3)
            );

            CREATE TABLE IF NOT EXISTS words (
                id      INTEGER PRIMARY KEY,
                eng     TEXT NOT NULL UNIQUE,
                rus     TEXT NOT NULL,
                example TEXT
            );

            CREATE TABLE IF NOT EXISTS user_words (
                user_id INTEGER NOT NULL REFERENCES users(id),
                word_id INTEGER NOT NULL REFERENCES words(id),
                day     TEXT NOT NULL,
                lvl     INTEGER DEFAULT 0,
                PRIMARY KEY (user_id, word_id)
            );

            CREATE TABLE IF NOT EXISTS ogg (
                id      INTEGER PRIMARY KEY,
                word_id INTEGER NOT NULL REFERENCES words(id),
                data    BLOB NOT NULL
            );

            CREATE TABLE IF NOT EXISTS vid (
                id      INTEGER PRIMARY KEY,
                word_id INTEGER NOT NULL REFERENCES words(id),
                data    BLOB NOT NULL,
                sub     TEXT
            );
        """)
        await conn.commit()


async def check_user(user_name: str, db_path: str = DB_PATH) -> bool:
    """Returns True if user existed, False if just created."""
    async with aiosqlite.connect(db_path) as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT id FROM users WHERE name = ?", (user_name,))
            row = await cur.fetchone()
            if row:
                return True
            await cur.execute("INSERT INTO users (name) VALUES (?)", (user_name,))
            await conn.commit()
            return False


async def _get_user_id(cur: aiosqlite.Cursor, user_name: str) -> int | None:
    await cur.execute("SELECT id FROM users WHERE name = ?", (user_name,))
    row = await cur.fetchone()
    return row[0] if row else None


async def add_to_db(
    user_name: str,
    words: List[Tuple[str, str, str]],
    db_path: str = DB_PATH
) -> bool:
    """Add words to global words table and link them to user."""
    try:
        today = datetime.today().isoformat()[:10]
        async with aiosqlite.connect(db_path) as conn:
            async with conn.cursor() as cur:
                user_id = await _get_user_id(cur, user_name)
                if not user_id:
                    return False

                for eng, rus, example in words:
                    # Insert word globally, ignore if exists
                    await cur.execute(
                        """INSERT OR IGNORE INTO words (eng, rus, example)
                           VALUES (?, ?, ?)""",
                        (eng, rus, example)
                    )
                    await cur.execute(
                        "SELECT id FROM words WHERE eng = ?", (eng,)
                    )
                    word_id = (await cur.fetchone())[0]

                    # Link to user
                    await cur.execute(
                        """INSERT OR REPLACE INTO user_words (user_id, word_id, day)
                           VALUES (?, ?, ?)""",
                        (user_id, word_id, today)
                    )

                await conn.commit()
        return True
    except Exception as e:
        return False


async def del_from_db(
    user_name: str,
    command_args: Tuple[bool, Tuple[int]],
    db_path: str = DB_PATH
) -> bool:
    """Delete by word IDs or by day numbers."""
    try:
        async with aiosqlite.connect(db_path) as conn:
            async with conn.cursor() as cur:
                user_id = await _get_user_id(cur, user_name)
                if not user_id:
                    return False

                by_day, ids = command_args

                if not by_day:
                    placeholders = ",".join("?" * len(ids))
                    await cur.execute(
                        f"""DELETE FROM user_words
                            WHERE user_id = ? AND word_id IN ({placeholders})""",
                        (user_id, *ids)
                    )
                else:
                    # Get ordered unique days for this user
                    await cur.execute(
                        """SELECT DISTINCT day FROM user_words
                           WHERE user_id = ? ORDER BY day""",
                        (user_id,)
                    )
                    unique_days = [r[0] for r in await cur.fetchall()]
                    total = len(unique_days)

                    days_for_del = [
                        unique_days[d - 1]
                        for d in ids
                        if 1 <= d <= total
                    ]
                    if not days_for_del:
                        return True

                    placeholders = ",".join("?" * len(days_for_del))
                    await cur.execute(
                        f"""DELETE FROM user_words
                            WHERE user_id = ? AND day IN ({placeholders})""",
                        (user_id, *days_for_del)
                    )

                await conn.commit()
        return True
    except Exception as e:
        print(f"Error during deletion: {e}")
        return False


async def get_word(
    user_name: str,
    n: int = 1,
    db_path: str = DB_PATH
) -> list[WordRow] | None:
    """Get n random words for user."""
    async with aiosqlite.connect(db_path) as conn:
        async with conn.cursor() as cur:
            user_id = await _get_user_id(cur, user_name)
            if not user_id:
                return None

            await cur.execute(
                """SELECT w.id, w.eng, w.rus, w.example, uw.day, uw.lvl
                   FROM user_words uw
                   JOIN words w ON w.id = uw.word_id
                   WHERE uw.user_id = ?""",
                (user_id,)
            )
            rows = await cur.fetchall()

        if not rows:
            return None

        sample = random.sample(rows, min(n, len(rows)))
        return [WordRow(*r) for r in sample]


async def get_day(
    user_name: str,
    days: Tuple[int],
    db_path: str = DB_PATH
) -> dict[int, list[WordRow]]:
    """Return {day_number: [WordRow,...]}"""
    result = {}
    async with aiosqlite.connect(db_path) as conn:
        async with conn.cursor() as cur:
            user_id = await _get_user_id(cur, user_name)
            if not user_id:
                return result

            await cur.execute(
                """SELECT DISTINCT day FROM user_words
                   WHERE user_id = ? ORDER BY day""",
                (user_id,)
            )
            unique_days = [r[0] for r in await cur.fetchall()]
            day_mapping = {idx + 1: day for idx, day in enumerate(unique_days)}

            for day_index in days:
                if day_index not in day_mapping:
                    continue
                target_day = day_mapping[day_index]

                await cur.execute(
                    """SELECT w.id, w.eng, w.rus, w.example, uw.day, uw.lvl
                       FROM user_words uw
                       JOIN words w ON w.id = uw.word_id
                       WHERE uw.user_id = ? AND uw.day = ?
                       ORDER BY w.id""",
                    (user_id, target_day)
                )
                rows = await cur.fetchall()
                result[day_index] = [WordRow(*r) for r in rows]

    return result


async def get_all(
    user_name: str,
    db_path: str = DB_PATH
) -> dict[int, list[WordRow]]:
    """Return all user words {day_number: [WordRow,...]}"""
    result = defaultdict(list)
    async with aiosqlite.connect(db_path) as conn:
        async with conn.cursor() as cur:
            user_id = await _get_user_id(cur, user_name)
            if not user_id:
                return {}

            await cur.execute(
                """SELECT w.id, w.eng, w.rus, w.example, uw.day, uw.lvl
                   FROM user_words uw
                   JOIN words w ON w.id = uw.word_id
                   WHERE uw.user_id = ?
                   ORDER BY uw.day, w.id""",
                (user_id,)
            )
            rows = await cur.fetchall()

        unique_days = sorted(set(r[4] for r in rows))
        day_to_index = {day: idx + 1 for idx, day in enumerate(unique_days)}

        for row in rows:
            day_index = day_to_index[row[4]]
            result[day_index].append(WordRow(*row))

    return dict(result)


async def check_word(
    user_name: str,
    word: str,
    db_path: str = DB_PATH
) -> list[WordRow]:
    async with aiosqlite.connect(db_path) as conn:
        async with conn.cursor() as cur:
            user_id = await _get_user_id(cur, user_name)
            if not user_id:
                return []

            await cur.execute(
                """SELECT w.id, w.eng, w.rus, w.example, uw.day, uw.lvl
                   FROM user_words uw
                   JOIN words w ON w.id = uw.word_id
                   WHERE uw.user_id = ? AND w.eng = ?""",
                (user_id, word)
            )
            rows = await cur.fetchall()
    return [WordRow(*r) for r in rows]


async def word_extra(
    word_id: int,
    db_path: str = DB_PATH
) -> ExtraRow | None:
    """Return audio and all videos for a word."""
    async with aiosqlite.connect(db_path) as conn:
        async with conn.cursor() as cur:
            # Audio (one per word)
            await cur.execute(
                "SELECT data FROM ogg WHERE word_id = ?", (word_id,)
            )
            ogg_row = await cur.fetchone()
            ogg_data = ogg_row[0] if ogg_row else None

            # Videos (multiple per word)
            await cur.execute(
                "SELECT id, data, sub FROM vid WHERE word_id = ?", (word_id,)
            )
            vid_rows = await cur.fetchall()
            videos = [VideoRow(*r) for r in vid_rows]

    if not ogg_data and not videos:
        return None

    return ExtraRow(ogg_data=ogg_data, videos=videos)


async def save_ogg(word_id: int, data: bytes, db_path: str = DB_PATH) -> None:
    async with aiosqlite.connect(db_path) as conn:
        await conn.execute(
            "INSERT INTO ogg (word_id, data) VALUES (?, ?)",
            (word_id, data)
        )
        await conn.commit()


async def add_video(word_id: int, video_path: str, sub: str = None, db_path: str = DB_PATH) -> None:
    with open(video_path, "rb") as f:
        video_bytes = f.read()
    
    async with aiosqlite.connect(db_path) as conn:
        await conn.execute(
            "INSERT INTO vid (word_id, data, sub) VALUES (?, ?, ?)",
            (word_id, video_bytes, sub)
        )
        await conn.commit()