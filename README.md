# Gemini Telegram Bot

A Telegram bot that answers in Russian using Google Gemini — plus a queue-driven autoposter for running your own content channel.

[![Python](https://img.shields.io/badge/python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![python-telegram-bot](https://img.shields.io/badge/python--telegram--bot-21.7-2CA5E0?logo=telegram&logoColor=white)](https://python-telegram-bot.org/)
[![google-generativeai](https://img.shields.io/badge/google--generativeai-0.8.3-4285F4?logo=google&logoColor=white)](https://ai.google.dev/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)
[![Deploy](https://img.shields.io/badge/deploy-Heroku-430098?logo=heroku&logoColor=white)](https://www.heroku.com/)

[Features](#key-features) · [Quick Start](#getting-started) · [Architecture](#project-structure)

---

<div align="center">
  <img src=".github/hero.png" alt="Bot channel preview" width="600" />
  <br />
  <em>Placeholder — replace with a screenshot of the bot's chat or channel posts.</em>
</div>

---

## Key Features

- 🤖 **Gemini-powered chat replies** — every text message is forwarded to a Gemini model (`generate_content_async`) with a system instruction that forces Russian-language answers, so the bot works as a drop-in AI assistant in any chat.
- ⚙️ **Configurable model** — the Gemini model name is read from the `GEMINI_MODEL` environment variable (defaults to `gemini-3.8-flash`), so you can swap models without touching code.
- 🛡️ **Graceful failure handling** — Gemini/API errors are caught per-message and logged (`logger.exception`), and the user gets a friendly Russian error message instead of a crash or silence.
- 👋 **`/start` onboarding** — a dedicated `CommandHandler` sends a welcome message explaining what the bot does.
- 📬 **Queue-based channel autoposting** — `post_next.py` pops the next entry from `posts_queue.txt` (entries separated by `===`), optionally attaches an image via an `IMAGE:` prefix line, publishes it to the configured channel, and rewrites the queue with the remaining posts — ideal for a cron/scheduled job.
- ✉️ **One-off manual posting** — `post_to_channel.py` sends a single ad-hoc message to the channel straight from the command line.

## Tech Stack

| Technology | Used for |
|---|---|
| [Python](https://www.python.org/) 3.10+ | Runtime |
| [python-telegram-bot](https://python-telegram-bot.org/) 21.7 | Telegram Bot API — polling, command/message handlers |
| [google-generativeai](https://ai.google.dev/) 0.8.3 | Gemini API client for AI-generated replies |
| Procfile (Heroku-style) | Worker-dyno process declaration for deployment |

## Getting Started

```bash
git clone https://github.com/Tonxetyz/gemini-telegram-bot.git
cd gemini-telegram-bot
pip install -r requirements.txt
```

### Environment variables

| Variable | Required | Description |
|---|---|---|
| `TELEGRAM_BOT_TOKEN` | yes | Bot token issued by [@BotFather](https://t.me/BotFather) |
| `GEMINI_API_KEY` | yes | API key for the Gemini API |
| `GEMINI_MODEL` | no | Overrides the Gemini model, default `gemini-3.8-flash` |

### Run the bot

```bash
python bot.py
```

### Post to the channel

```bash
# publish a single ad-hoc message
python post_to_channel.py "текст поста"

# publish the next queued entry from posts_queue.txt
python post_next.py
```

### Run the tests

```bash
python test_bot.py
```

## Project Structure

```
gemini-telegram-bot/
├── bot.py               # Entry point — polling bot with Gemini-powered replies
├── post_to_channel.py   # CLI script — posts a single ad-hoc message to the channel
├── post_next.py         # Pops and publishes the next entry from posts_queue.txt (supports images)
├── posts_queue.txt      # Plain-text queue of scheduled channel posts, separated by "==="
├── test_bot.py          # Self-contained async test harness for bot.py's handlers
├── requirements.txt     # Python dependencies
├── Procfile             # Heroku worker process declaration
├── avatar.png           # Bot/channel avatar image
└── .gitignore           # Excludes __pycache__, *.pyc, .env
```

## License

[MIT](./LICENSE)
