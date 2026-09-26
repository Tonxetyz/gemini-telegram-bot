# Gemini Telegram Bot

Telegram-бот на python-telegram-bot, который пересылает сообщения пользователя в Gemini и отвечает на русском.

## Стек

Python, `python-telegram-bot`, `google-generativeai`.

## Запуск

```bash
pip install -r requirements.txt
export TELEGRAM_BOT_TOKEN=...
export GEMINI_API_KEY=...
python bot.py
```

`GEMINI_MODEL` (опционально) — переопределяет модель, по умолчанию `gemini-3.8-flash`.

## Деплой

`Procfile` настроен для Heroku-подобных платформ (`worker: python bot.py`).

## Тесты

```bash
python -m pytest test_bot.py
```
