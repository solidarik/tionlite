import asyncio
import sys

from config import config
from tion_api import TionApi

if __name__ == "__main__":

    name = "Bedroom Device"
    bedroom_config = config.get_device('bedroom')

    if not bedroom_config['IN_USE']:
        print(f"{name} is disabled now")
        sys.exit(0)

    print(f"Switching {name} to evening mode")

    fan_speed = bedroom_config['evening']['fan_speed']
    heater_temp = bedroom_config['evening']['heater_temp']

    bedroom = TionApi(bedroom_config['DEVICE_ID'])
    asyncio.run(bedroom.change_params(fan_speed=fan_speed, heater_temp=heater_temp))
