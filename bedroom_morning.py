import asyncio
import sys

from config import Config
from tion_api import TionApi

if __name__ == "__main__":

    name = "Bedroom Device"

    if not Config.IS_USE_BEDROOM:
        print(f"{name} is disabled now")
        sys.exit(0)

    print(f"Switching {name} to morning mode")

    fan_speed = Config.FUN_SPEED_MORNING

    bedroom = TionApi(Config.BEDROOM_DEVICE_ID)
    asyncio.run(bedroom.change_params(fan_speed=fan_speed, heater_temp=0))
