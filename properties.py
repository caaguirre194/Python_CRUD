import configparser

config = configparser.RawConfigParser()
config.read('config.properties')

def getConfigSection(section_name):
    return dict(config.items(section_name))

def getConfig():
    if not hasattr(getConfig, 'section_dict'):
        getConfig.section_dict = dict()

        for section in config.sections():
            getConfig.section_dict[section] = dict(config.items(section))

    return getConfig.section_dict
