import asyncio

from config import Config
from tion_api import TionApi

async def main():
    device_ids = [Config.KAMILLA_DEVICE_ID, Config.BEDROOM_DEVICE_ID]
    for device_id in device_ids:
        device = TionApi(device_id)
        await device.switch_on()

if __name__ == "__main__":
    print("Switch Off Devices")
    asyncio.run(main())
