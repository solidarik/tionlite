import asyncio

from config import Config
from tion_api import TionApi

if __name__ == "__main__":
    print("Start App")
    bedroom = TionApi(Config.BEDROOM_DEVICE_ID)
    kamilla = TionApi(Config.KAMILLA_DEVICE_ID)

    # asyncio.run(bedroom.get_info(bedroom))
    asyncio.run(kamilla.pair())
