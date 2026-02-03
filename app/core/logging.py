import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setFormatter(
    logging.Formatter(
        "%(asctime)s | %(levelname)s | "
        "%(filename)s:%(lineno)d | "
        "%(funcName)s() | %(message)s"
    )
)

logger.addHandler(console_handler)