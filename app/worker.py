from app.manager import manager
from app.logs import logger


async def start() -> None:
    try:
        await manager.clear_redis()
    except Exception as _ex:
        logger.info(_ex)
