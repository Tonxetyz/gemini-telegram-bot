import asyncio
import os
import sys

from telegram import Bot

CHANNEL = "@Botnozx"


async def post(text: str) -> None:
    bot = Bot(token=os.environ["TELEGRAM_BOT_TOKEN"])
    await bot.send_message(chat_id=CHANNEL, text=text)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python post_to_channel.py \"текст поста\"")
    asyncio.run(post(sys.argv[1]))
