import asyncio
import os
import sys
from pathlib import Path

from telegram import Bot

CHANNEL = "@Botnozx"
QUEUE_FILE = Path(__file__).parent / "posts_queue.txt"
DELIMITER = "\n===\n"


async def post(text: str, image_path: str | None) -> None:
    bot = Bot(token=os.environ["TELEGRAM_BOT_TOKEN"])
    if image_path:
        with open(Path(__file__).parent / image_path, "rb") as photo:
            await bot.send_photo(chat_id=CHANNEL, photo=photo)
    await bot.send_message(chat_id=CHANNEL, text=text)


def parse_entry(entry: str) -> tuple[str, str | None]:
    entry = entry.strip()
    if entry.startswith("IMAGE:"):
        image_line, _, rest = entry.partition("\n")
        return rest.strip(), image_line.removeprefix("IMAGE:").strip()
    return entry, None


def main() -> None:
    content = QUEUE_FILE.read_text(encoding="utf-8").strip()
    if not content:
        sys.exit("Очередь пуста — попроси Claude сгенерировать ещё постов.")

    posts = content.split(DELIMITER)
    next_post, remaining = posts[0], posts[1:]
    text, image_path = parse_entry(next_post)

    asyncio.run(post(text, image_path))

    QUEUE_FILE.write_text(DELIMITER.join(remaining).strip() + "\n", encoding="utf-8")
    print(f"Опубликовано, осталось постов в очереди: {len(remaining)}")


if __name__ == "__main__":
    main()
