import logging
import sys

DEFAULT_LOG_FORMAT = "[%(asctime)s][%(levelname)s][%(name)s.%(funcName)s:%(lineno)d] %(message)s"
DEFAULT_DATE_FORMAT = "%H:%M:%S"
DEFAULT_LOG_LEVEL = logging.INFO


def setup_logger(name, level=DEFAULT_LOG_LEVEL):
    """
    """
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(DEFAULT_LOG_FORMAT, DEF))

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
