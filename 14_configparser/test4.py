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


def interpolationDemo(path):
    if not os.path.exists(path):
        createConfig(path)

    config = configparser.ConfigParser()
    config.read(path)

    print(config.get("Settings", "font_info"))
    print(config.get("Settings", "font_info", vars={"font":"Arial", "font_size":"100"}))


if __name__ == "__main__":
    path = "settings.ini"
    interpolationDemo(path)