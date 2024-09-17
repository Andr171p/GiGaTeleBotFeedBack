import sys

from loguru import logger


logger.add(
    sys.stderr,
    format="{time} {level} {message}",
    filter="sub.module",
    level="INFO"
)


class AppLogs:
    SUCCESSFUL_CLEAR_REDIS = "REDIS CLEAR SUCCESSFULLY"
