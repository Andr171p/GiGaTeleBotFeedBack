from storage.connect import RedisConnection

from app.timing import schedule
from app.logs import (
    logger,
    AppLogs
)


class RedisManager(RedisConnection):
    async def delete_keys(self) -> None:
        await self.connect()
        await self.redis.flushdb()
        logger.info(AppLogs.SUCCESSFUL_CLEAR_REDIS)
        await self.close()

    async def clear_redis(self) -> None:
        now = await schedule.set_time()
        if await schedule.check_time(now=now):
            await self.delete_keys()
        await schedule.wait()


manager = RedisManager()
