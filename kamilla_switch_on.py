import asyncio
import sys

from config import config
from tion_api import TionApi

if __name__ == "__main__":

    name = "Kamilla Device"
    kamilla_config = config.get_device('kamilla')

    if not kamilla_config['IN_USE']:
        print(f"{name} is disabled now")
        sys.exit(0)

    print("Switch On Kamilla Device")
    device = TionApi(kamilla_config['DEVICE_ID'])
    asyncio.run(device.switch_on())
