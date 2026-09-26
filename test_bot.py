import asyncio
import types

import bot


class FakeMessage:
    def __init__(self, text):
        self.text = text
        self.replies = []

    async def reply_text(self, text):
        self.replies.append(text)


async def run_case(fake_generate, expect_error):
    message = FakeMessage("привет")
    update = types.SimpleNamespace(message=message)
    bot.model.generate_content_async = fake_generate
    await bot.handle_message(update, None)
    if expect_error:
        assert "ошибка" in message.replies[0].lower()
    else:
        assert message.replies[0] == "ok"


async def ok_gen(_):
    return types.SimpleNamespace(text="ok")


async def fail_gen(_):
    raise RuntimeError("boom")


async def run_start_case():
    message = FakeMessage("/start")
    update = types.SimpleNamespace(message=message)
    await bot.handle_start(update, None)
    assert message.replies[0] == bot.WELCOME_TEXT


async def main():
    await run_case(ok_gen, expect_error=False)
    await run_case(fail_gen, expect_error=True)
    await run_start_case()
    print("OK")


if __name__ == "__main__":
    asyncio.run(main())
