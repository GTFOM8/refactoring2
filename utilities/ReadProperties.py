import configparser
import os

this_folder = os.path.dirname(os.path.abspath(__file__))
init_file = os.path.join(this_folder, 'config_template.ini')

config = configparser.RawConfigParser()
config.read(init_file)


class ReadConfig:
    @staticmethod
    def get_testrail_host():
        testrail_host = config.get('common_info', 'testrail_host')
        return testrail_host

    @staticmethod
    def get_testrail_login():
        testrail_login = config.get('common_info', 'testrail_login')
        return testrail_login

    @staticmethod
    def get_testrail_pass():
        testrail_pass = config.get('common_info', 'testrail_pass')
        return testrail_pass
