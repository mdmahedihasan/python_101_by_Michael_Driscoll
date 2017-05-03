import logging


logging.basicConfig(filename="sample.log", level=logging.INFO)
logging.debug("this is a debug message")
logging.info("informational message")
logging.error("an error has happened!")