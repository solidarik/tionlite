from tion_btle import TionLite


class TionApi:

    def __init__(self, mac_id: str):
        super().__init__()
        self.device = TionLite(mac=mac_id)

    async def get_info(self):
        print(await self.device.get())

    async def pair(self):
        await self.device.pair()
        print("Successful")

    async def switch_on(self):
        await self.device.set({"state": "on"})

    async def switch_off(self):
        await self.set({"state": "off"})

    async def change_params(self, *, fan_speed: int, heater_temp: int = 12):
        await self.device.set(
            {
                "state": "on",
                "fan_speed": fan_speed,
                "heater_temp": heater_temp,
                "heater": "on",
            }
        )
