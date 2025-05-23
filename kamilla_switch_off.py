import asyncio
import sys

from config import Config
from tion_api import TionApi

if __name__ == "__main__":

    name = "Kamilla Device"

    if not Config.IS_USE_KAMILLA:
        print(f"{name} is disabled now")
        sys.exit(0)

    print("Switch Off Kamilla Device")
    device = TionApi(Config.KAMILLA_DEVICE_ID)
    asyncio.run(device.switch_off())
