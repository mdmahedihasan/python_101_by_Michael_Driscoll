import logging
import otherMod2


def main():
    """
    the main entry point of the application
    :return: 
    """
    logger = logging.getLogger("exampleApp")
    logger.setLevel(logging.INFO)

    # create the logging file handler
    file_handler = logging.FileHandler("new_snake.log")
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    # add handler to logger object
    logger.addHandler(file_handler)

    logger.info("Program started")
    result = otherMod2.add(7, 8)
    logger.info("Done")


if __name__ == '__main__':
    main()