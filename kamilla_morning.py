import asyncio
import sys

from config import Config
from tion_api import TionApi

if __name__ == "__main__":

    name = "Kamilla Device"

    if not Config.IS_USE:
        print(f"{name} is disabled now")
        sys.exit(0)

    print("Switching Kamilla Device to morning mode")
    device = TionApi(Config.KAMILLA_DEVICE_ID)
    asyncio.run(device.change_params(fan_speed=2, heater_temp=0))
