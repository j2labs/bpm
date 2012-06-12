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


