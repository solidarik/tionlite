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

    fan_speed = kamilla_config['morning']['fan_speed']
    heater_temp = kamilla_config['morning']['heater_temp']

    print("Switching Kamilla Device to morning mode")
    device = TionApi(kamilla_config['DEVICE_ID'])
    asyncio.run(device.change_params(fan_speed=fan_speed, heater_temp=heater_temp))
