import logging

DEFAULT_LOG_FORMAT = "%(asctime)s %(levelname) -7s " "%(name)s: %(message)s"
DEFAULT_LOG_LEVEL = logging.INFO
# DEFAULT_LOG_FILE = "app.log"


def setup_logger(name, level=DEFAULT_LOG_LEVEL):
    """

    """
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(DEFAULT_LOG_FORMAT))

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
