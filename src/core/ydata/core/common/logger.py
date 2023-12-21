import logging
from typing import TextIO
import sys


def create_logger(name, stream: TextIO = sys.stdout, level=logging.INFO):
  handler = logging.StreamHandler(stream)
  handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(module)s:%(lineno)d | %(message)s"))

  logger = logging.getLogger(name)
  logger.setLevel(level)
  logger.addHandler(handler)
  logger.propagate = False

  return logger
