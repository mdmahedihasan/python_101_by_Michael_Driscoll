import configobj


def createConfig(path):
    config = configobj.ConfigObj()
    config.filename = path
    config["sony"] = {}
    config["sony"]["product"] = "sony ps3"
    config["sony"]["accesories"] = ["controller", "eye", "memory_stick"]
    config["sony"]["retail price"] = "$400"
    config.write()


if __name__ == '__main__':
    createConfig("new.ini")