import os
from configobj import ConfigObj

current_path = os.path.dirname(__file__)
cfg_path = os.path.join(current_path, '../conf/local_config.ini')

class ConfigUtils:
    def __init__(self, conf_path=cfg_path):
        self.__conf = ConfigObj(conf_path, encoding='utf-8')
    def read_ini(self, sec, option):
        value = self.__conf[sec][option]
        return value
    @property
    def get_url_path(self):
        value = self.read_ini('default', 'URL')
        return value
    @property
    def get_title_path(self):
        value = self.read_ini('default', 'title')
        return value
config = ConfigUtils()

if __name__=='__main__':
    config_u = ConfigUtils()
    print(config_u.get_url_path)
    print(config_u.get_title_path)