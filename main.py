from config import config
from tion_api import TionApi
import asyncio

if __name__ == "__main__":
    print("Start App")
    bedroom_config = config.get_device('bedroom')
    kamilla_config = config.get_device('kamilla')
    bedroom = TionApi(bedroom_config['DEVICE_ID'])
    kamilla = TionApi(kamilla_config['DEVICE_ID'])

    # asyncio.run(bedroom.get_info(bedroom))
    asyncio.run(kamilla.pair())
