import configparser
import os


def createConfig(path):
    """
    create a config file
    :param path: 
    :return: 
    """
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "font", "Courier")
    config.set("Settings", "font_size", "10")
    config.set("Settings", "font_style", "Normal")
    config.set("Settings", "font_info", "You are using %(font)s at %(font_size)s pt")

    with open(path, "w") as config_file:
        config.write(config_file)


def crudConfig(path):
    """
    create, read, update, delete config
    :param path: 
    :return: 
    """
    if not os.path.exists(path):
        createConfig(path)

    config = configparser.ConfigParser()
    config.read(path)

    # read value
    font = config.get("Settings", "font")
    font_size = config.get("Settings", "font_size")

    # change value
    config.set("Settings", "font_size", "12")

    # delete value
    config.remove_option("Settings", "font_style")

    # write changes
    with open(path, "w") as cofig_file:
        config.write(cofig_file)

if __name__ == "__main__":
    path = "settings.ini"
    crudConfig(path)