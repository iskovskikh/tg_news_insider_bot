import asyncio
import logging
import logging.config

from aiogram import Dispatcher, Bot
from punq import Container

from application.handlers.main_router import router as main_router
from logic.container import get_container
from settings.config import Config
from settings.logger import get_logger_config

logger = logging.getLogger(__name__)


async def main():
    container: Container = get_container()
    config: Config = container.resolve(Config)
    logging.config.dictConfig(get_logger_config(config=config))

    logger.info("Init routers.")

    dp: Dispatcher = container.resolve(Dispatcher)
    dp.include_router(main_router)

    bot: Bot = container.resolve(Bot)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
