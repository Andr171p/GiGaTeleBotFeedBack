import pytz
import asyncio
import datetime

from app.config import (
    Timings,
    Timezones,
    SleepTime
)


class TimeSchedule:
    timezone = pytz.timezone(Timezones.TIMEZONE)
    wait_time = SleepTime.TIME

    @classmethod
    async def set_time(cls) -> datetime.datetime:
        now = datetime.datetime.now(cls.timezone)
        return now

    @staticmethod
    async def check_time(now: datetime.datetime) -> bool:
        hours = Timings.HOURS
        minutes = Timings.MINUTES
        seconds = Timings.SECONDS
        if now.hour == hours and now.minute == minutes and now.second == seconds:
            return True
        else:
            return False

    @classmethod
    async def wait(cls) -> None:
        await asyncio.sleep(cls.wait_time)


schedule = TimeSchedule()
