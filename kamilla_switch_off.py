import asyncio

from config import Config
from tion_api import TionApi

if __name__ == "__main__":
    print("Switch Off Kamilla Device")
    device = TionApi(Config.KAMILLA_DEVICE_ID)
    asyncio.run(device.switch_off())
