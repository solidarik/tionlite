import asyncio

from config import Config
from tion_api import TionApi

if __name__ == "__main__":
    print("Start App")
    bedroom = TionApi(Config.BEDROOM_DEVICE_ID)
    kamilla = TionApi(Config.KAMILLA_DEVICE_ID)

    # asyncio.run(morning_change(device=bedroom, fanspeed=2))
    # asyncio.run(morning_change(device=kamilla, fanspeed=2))

    # asyncio.run(evening_change(device=bedroom, fanspeed=1))
    # asyncio.run(evening_change(device=kamilla, fanspeed=1))

    # asyncio.run(get_info_device(bedroom))
    # asyncio.run(pair_device(bedroom))
    asyncio.run(bedroom.get_info())
