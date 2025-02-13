import asyncio

from config import Config
from tion_api import TionApi

if __name__ == "__main__":
    print("Switching Kamilla Device to morning mode")
    device = TionApi(Config.KAMILLA_DEVICE_ID)
    asyncio.run(device.change_params(fan_speed=2, heater_temp=20))
