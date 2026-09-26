import asyncio
import os
import sys
from pathlib import Path

from telegram import Bot

CHANNEL = "@Botnozx"
QUEUE_FILE = Path(__file__).parent / "posts_queue.txt"
DELIMITER = "\n===\n"


async def post(text: str) -> None:
    bot = Bot(token=os.environ["TELEGRAM_BOT_TOKEN"])
    await bot.send_message(chat_id=CHANNEL, text=text)


def main() -> None:
    content = QUEUE_FILE.read_text(encoding="utf-8").strip()
    if not content:
        sys.exit("Очередь пуста — попроси Claude сгенерировать ещё постов.")

    posts = content.split(DELIMITER)
    next_post, remaining = posts[0].strip(), posts[1:]

    asyncio.run(post(next_post))

    QUEUE_FILE.write_text(DELIMITER.join(remaining).strip() + "\n", encoding="utf-8")
    print(f"Опубликовано, осталось постов в очереди: {len(remaining)}")


if __name__ == "__main__":
    main()
