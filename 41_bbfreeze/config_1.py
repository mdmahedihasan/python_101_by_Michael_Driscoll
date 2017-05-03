import configobj


def createConfig(configFile):
    config = configobj.ConfigObj()
    inifile = configFile
    config.filename = inifile
    config["server"] = "http://www.google.com"
    config["username"] = "mike"
    config["password"] = "dingbat"
    config["update interval"] = 2
    config.write()


def getConfig(configFile):
    """open the config file and return a configobj"""
    return configobj.ConfigObj(configFile)


def createConfig2(path):
    config = configobj.ConfigObj()
    config.filename = path
    config["sony"] = {}
    config["sony"]["product"] = "sony ps3"
    config.write()


if __name__ == '__main__':
    createConfig2("sampleConfig2.ini")