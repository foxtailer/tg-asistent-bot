import asyncio
import aiosqlite

OLD_DB = "bot_db.db"
NEW_DB = "bot_db2.db"

USER_TABLES = ["Mari", "攻殻機動隊"]


async def migrate():
    async with aiosqlite.connect(OLD_DB) as old, aiosqlite.connect(NEW_DB) as new:
        # Инициализируем новую схему
        await new.executescript("""
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
        await new.commit()

        for user_name in USER_TABLES:
            print(f"Migrating user: {user_name}")

            # Создаём юзера в новой базе
            await new.execute(
                "INSERT OR IGNORE INTO users (name) VALUES (?)", (user_name,)
            )
            await new.commit()

            async with new.execute(
                "SELECT id FROM users WHERE name = ?", (user_name,)
            ) as cur:
                user_id = (await cur.fetchone())[0]

            # Читаем слова из старой таблицы юзера
            async with old.execute(
                f"SELECT eng, rus, example, day, lvl FROM {user_name}"
            ) as cur:
                rows = await cur.fetchall()

            print(f"  Found {len(rows)} words")

            for eng, rus, example, day, lvl in rows:
                # Вставляем слово глобально
                await new.execute(
                    "INSERT OR IGNORE INTO words (eng, rus, example) VALUES (?, ?, ?)",
                    (eng, rus, example)
                )

                async with new.execute(
                    "SELECT id FROM words WHERE eng = ?", (eng,)
                ) as cur:
                    word_id = (await cur.fetchone())[0]

                # Связываем юзера со словом
                await new.execute(
                    """INSERT OR REPLACE INTO user_words (user_id, word_id, day, lvl)
                       VALUES (?, ?, ?, ?)""",
                    (user_id, word_id, day, lvl)
                )

            await new.commit()
            print(f"  Done: {user_name}")

        print("\nMigration complete!")

        # Проверка
        async with new.execute("SELECT COUNT(*) FROM words") as cur:
            print(f"Total unique words: {(await cur.fetchone())[0]}")
        async with new.execute("SELECT COUNT(*) FROM user_words") as cur:
            print(f"Total user-word links: {(await cur.fetchone())[0]}")


asyncio.run(migrate())