import logging
import otherMod


def main():
    """
    the main entry point of the application
    :return: 
    """
    logging.basicConfig(filename="mySnake.log", level=logging.INFO)
    logging.INFO("Program started")
    result = otherMod.add(7, 8)
    logging.INFO("Done")


if __name__ == '__main__':
    main()