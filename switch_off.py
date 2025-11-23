import asyncio

from config import config
from tion_api import TionApi

async def main():
    for device_name in ['kamilla', 'bedroom']:
        device_config = config.get_device(device_name)
        if device_config['IN_USE']:
            device = TionApi(device_config['DEVICE_ID'])
            await device.switch_off()

if __name__ == "__main__":
    print("Switch Off Devices")
    asyncio.run(main())
