import os


###
### Foundational Settings
###

cwd = os.path.dirname(__file__)
dir_project = os.path.abspath(os.path.dirname(cwd))  ### cwd/../


###
### Directory Arrangement
###

dir_bin = os.path.join(dir_project, 'bin/')
dir_virtualenv = os.path.join(dir_project, '.virtualenv/')
dir_settings = os.path.join(dir_project, 'settings/')
dir_logs = os.path.join(dir_project, '.var/log/')
dir_static = os.path.join(dir_project, 'static/')
dir_templates = os.path.join(dir_project, 'templates/')


###
### Mongrel2
###

mongrel2_conf = os.path.join(dir_settings, 'settings/mongrel2.conf')
mongrel2_db = os.path.join(dir_settings, 'settings/mongrel2.db')
