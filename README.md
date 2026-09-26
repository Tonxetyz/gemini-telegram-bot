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

## Публикация в канал

```bash
export TELEGRAM_BOT_TOKEN=...
python post_to_channel.py "текст поста"
```

Постит в канал `@Botnozx` (бот должен быть там админом с правом Post Messages).

## Тесты

```bash
python -m pytest test_bot.py
```
