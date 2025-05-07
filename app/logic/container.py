from functools import lru_cache

from punq import Container, Scope

from settings.config import Config
from aiogram import Bot, Dispatcher

@lru_cache(maxsize=1)
def get_container() -> Container:
    return _init_container()


def _init_container() -> Container:
    container = Container()

    # config
    container.register(Config, instance=Config(), scope=Scope.singleton)
    config: Config = container.resolve(Config)

    # services
    container.register(Bot, instance=Bot(token=config.bot_token.get_secret_value()), scope=Scope.singleton)
    container.register(Dispatcher, instance=Dispatcher(), scope=Scope.singleton)

    return container
