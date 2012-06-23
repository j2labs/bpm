import os
import logging
from settings import constants


### Foundational Settings
cwd = os.path.dirname(__file__)
dir_project = os.path.abspath(os.path.dirname(cwd))  ### cwd/../
log_level = logging.DEBUG
cookie_secret = 'OMGSOOOOOSECRET'


### Directory Arrangement
dir_bin = os.path.join(dir_project, 'bin/')
dir_settings = os.path.join(dir_project, 'settings/')
dir_static = os.path.join(dir_project, 'static/')
dir_templates = os.path.join(dir_project, 'templates/')
dir_virtualenv = os.path.join(dir_project, '.virtualenv/')
dir_logs = os.path.join(dir_project, '.var/log/')
dir_run = os.path.join(dir_project, '.var/run/')
dir_sock = os.path.join(dir_project, '.var/sock/')


### Web Server
web_server = constants.MONGREL2
web_host = 'localhost'
web_port = 6767
