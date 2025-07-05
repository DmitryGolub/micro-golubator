import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

from aiogram.types import Message

from faststream.rabbit import RabbitBroker

from src.config import settings


dp = Dispatcher()
bot = Bot(token=settings.BOT_TOKEN)
broker = RabbitBroker(settings.RABBIT_URL)


@broker.subscriber("orders")
async def handle_orders_and_send_message(data: str):
    await bot.send_message(
        chat_id=5461886782,
        text=data
    )

@dp.message()
async def get_message(message: Message):
    await message.answer(f"{message.chat.id}")


async def main() -> None:
    logging.info("Connectin...")
    async with broker:
        await broker.start()
        logging.info("Broker was start")
        await dp.start_polling(bot)
    logging.info("Finished broker")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())