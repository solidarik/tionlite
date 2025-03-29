import asyncio

from config import Config
from tion_api import TionApi

if __name__ == "__main__":
    print("Switching Bedroom Device to evening mode")
    bedroom = TionApi(Config.BEDROOM_DEVICE_ID)
    asyncio.run(bedroom.change_params(fan_speed=2, heater_temp=16))
