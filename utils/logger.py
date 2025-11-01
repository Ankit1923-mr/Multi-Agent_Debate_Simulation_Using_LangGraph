import logging
from datetime import datetime

def setup_logger(log_filepath="logs/debate_log.txt"):
    logging.basicConfig(
        filename=log_filepath, filemode="a", level=logging.INFO,
        format="%(asctime)s %(levelname)s: %(message)s"
    )
    return logging.getLogger("DebateLogger")

def log_message(logger, message):
    print(message)
    logger.info(message)
