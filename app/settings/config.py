import os
from pathlib import Path

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from settings.base import PydanticBaseSettings, BASE_DIR


CONFIG_PATH = Path(os.environ.get("CONFIG", BASE_DIR / "config.yaml"))


class LogConfig(BaseSettings):
    path: Path = BASE_DIR / "logs"
    console_format: str = Field(
        # default="%(levelname) -10s %(asctime)s %(name) -30s %(module) -30s %(funcName) -35s %(lineno) -5d: %(message)s"
        default="%(asctime)s | %(levelname) -8s | %(message)s"
    )
    file_format: str = Field(
        default="%(levelname) -10s %(asctime)s %(name) -30s %(module) -30s %(funcName) -35s %(lineno) -5d: %(message)s"
    )


class Config(PydanticBaseSettings):
    model_config = SettingsConfigDict(
        yaml_file=CONFIG_PATH,
    )

    bot_token: SecretStr = Field(default="", alias="BOT_TOKEN")

    log: LogConfig = LogConfig()
