from functools import wraps
from typing import Awaitable, Callable, TypeVar

from tion_btle import TionLite

T = TypeVar("T")


def repeat_n_times(n: int):
    """
    Decorator factory to repeat an async function n times.
    """

    def decorator(
        async_func: Callable[..., Awaitable[T]],
    ) -> Callable[..., Awaitable[T]]:
        @wraps(async_func)
        async def wrapper(*args, **kwargs) -> T:
            for attempt in range(n):
                try:
                    result = await async_func(*args, **kwargs)
                    print(f"Attempt {attempt} succeeded with result: {result}")
                    return result  # Return the result if successful
                except Exception as e:
                    print(f"Attempt {attempt} failed with error: {e}")
                    # if attempt == n - 1:
                    #     raise
            raise RuntimeError("All attempts failed")  #

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

    @repeat_n_times(10)
    async def switch_on(self):
        await self.device.set({"state": "on"})

    @repeat_n_times(10)
    async def switch_off(self):
        await self.device.set({"state": "off"})

    @repeat_n_times(10)
    async def change_params(self, *, fan_speed: int, heater_temp: int = 12):
        await self.device.set(
            {
                "state": "on",
                "fan_speed": fan_speed,
                "heater_temp": heater_temp,
                "heater": "on" if heater_temp > 0 else "off",
            }
        )
