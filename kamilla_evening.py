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

    fan_speed = kamilla_config['evening']['fan_speed']
    heater_temp = kamilla_config['evening']['heater_temp']

    print(f"Switching {name} to evening mode")
    device = TionApi(kamilla_config['DEVICE_ID'])
    asyncio.run(device.change_params(fan_speed=fan_speed, heater_temp=heater_temp))
