from functools import wraps
from typing import Awaitable, Callable, TypeVar

from tion_btle import TionLite

T = TypeVar("T")


def repeat_n_times(n: int):
    """
    Decorator factory to repeat an async function n times.
    """

    def decorator(
        async_func: Callable[..., Awaitable[T]]
    ) -> Callable[..., Awaitable[T]]:
        @wraps(async_func)
        async def wrapper(*args, **kwargs) -> T:
            results = []
            for i in range(n):
                result = await async_func(*args, **kwargs)
                results.append(result)
                print(f"Call {i + 1} result: {result}")
            return results[-1]

        return wrapper

    return decorator


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

    @repeat_n_times(3)
    async def change_params(self, *, fan_speed: int, heater_temp: int = 12):
        await self.device.set(
            {
                "state": "on",
                "fan_speed": fan_speed,
                "heater_temp": heater_temp,
                "heater": "on",
            }
        )
