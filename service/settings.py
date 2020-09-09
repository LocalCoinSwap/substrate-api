import os

ENV_SETUP = os.getenv("ENV_SETUP", "production")

if ENV_SETUP == "local":
    from .config.local import *
else:
    from .config.production import *

SERVICE_NAME = "Kusama-api"


def get_config():
    class Config:
        pass

    return Config
