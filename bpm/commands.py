from uuid import uuid4
import argparse
import os
import os
import signal
import sqlite3
import subprocess
import sys


###
### Top-level Parsers
###

### BPM Parser
bpm_parser = argparse.ArgumentParser('Brubeck Project Manager')
bpm_subparsers = bpm_parser.add_subparsers(title='subcommands',
                                           description='valid subcommands',
                                           help='additional help')

bpm_parser.add_argument('--settings', default='settings.py')


### m2sh Parser
m2sh_parser = argparse.ArgumentParser(add_help=False)
m2sh_parser.add_argument('--host', default='localhost')
m2sh_parser.add_argument('-s', '--sudo', default=False)


###
### Project Subparser
###

### Imports
from bpm.project import project_create

### bpm project ...
project_parser = bpm_subparsers.add_parser('project')
project_subparsers = project_parser.add_subparsers()

### bpm project create <project_name>
project_parser_create = project_subparsers.add_parser('create')
project_parser_create.set_defaults(fn=project_create)
project_parser_create.add_argument('-n', '--name', default='brubeck_project/')


###
### Env Subparser
###

### Imports
from bpm.env import env_create

### bpm env ...
env_parser = bpm_subparsers.add_parser('env')
env_subparsers = env_parser.add_subparsers()

### bpm env create [-r|--requirements=<file>]
env_parser_create = env_subparsers.add_parser('create')
env_parser_create.set_defaults(fn=env_create)
env_parser_create.add_argument('-f', '--file', default=None)


###
### System Subparser
###

### Imports
from bpm.system import (system_run, system_status, system_load, system_start,
                        system_stop, system_log, system_reload)


### bpm system ...
system_parser = bpm_subparsers.add_parser('system')
system_subparsers = system_parser.add_subparsers()


### bpm system run <app_name>
run_parser = system_subparsers.add_parser('run')
run_parser.set_defaults(fn=system_run)
run_parser.add_argument('app_name', default='main')


### bpm system status
status_parser = system_subparsers.add_parser('status', parents=[m2sh_parser])
status_parser.set_defaults(fn=system_status)


### bpm system reload
restart_parser = system_subparsers.add_parser('reload', parents=[m2sh_parser])
restart_parser.set_defaults(fn=system_reload)


### bpm system load <conf_file>
load_parser = system_subparsers.add_parser('load', parents=[m2sh_parser])
load_parser.set_defaults(fn=system_load)
load_parser.add_argument('conf_file')


### bpm system start --foreground
start_parser = system_subparsers.add_parser('start', parents=[m2sh_parser])
start_parser.set_defaults(fn=system_start)
start_parser.add_argument('--foreground', action='store_true')


### bpm system stop
stop_parser = system_subparsers.add_parser('stop', parents=[m2sh_parser])
stop_parser.set_defaults(fn=system_stop)


### bpm system log
log_parser = system_subparsers.add_parser('log', parents=[m2sh_parser])
log_parser.set_defaults(fn=system_log)

