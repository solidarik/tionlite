import logging
import os

from dotenv import load_dotenv

path = ".env"
if not load_dotenv(path):
    logging.error("env file not loaded")
else:
    logging.info(f"env file {path} loaded")


class Config:
    LOG_FILE = os.environ.get("LOG_FILE", None)
    LOG_LEVEL = logging.DEBUG

    # Данные для почтового ящика
    BEDROOM_DEVICE_ID = os.environ.get("BEDROOM_DEVICE_ID", "")
    KAMILLA_DEVICE_ID = os.environ.get("KAMILLA_DEVICE_ID", "")

    FUN_SPEED_EVENING = int(os.environ.get("FUN_SPEED_EVENING", 1))
    FUN_SPEED_MORNING = int(os.environ.get("FUN_SPEED_MORNING", 2))

    BEDROOM_HEATER_TEMP = int(os.environ.get("BEDROOM_HEATER_TEMP", 12))
    KAMILLA_HEATER_TEMP = int(os.environ.get("KAMILLA_HEATER_TEMP", 12))

    IS_USE_BEDROOM = os.environ.get("IS_USE_BEDROOM", "false") not in ["false", "False"]
    IS_USE_KAMILLA = os.environ.get("IS_USE_KAMILLA", "false") not in ["false", "False"]
