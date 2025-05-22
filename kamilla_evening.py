import asyncio
import sys

from config import Config
from tion_api import TionApi

if __name__ == "__main__":

    name = "Kamilla Device"

    if not Config.IS_USE_KAMILLA:
        print(f"{name} is disabled now")
        sys.exit(0)

    fan_speed = Config.FUN_SPEED_EVENING
    heater_temp = Config.KAMILLA_HEATER_TEMP

    print(f"Switching {name} to evening mode")
    device = TionApi(Config.KAMILLA_DEVICE_ID)
    asyncio.run(device.change_params(fan_speed=fan_speed, heater_temp=heater_temp))
