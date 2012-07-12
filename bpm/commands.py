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
### Create Subparser
###

### Imports
from bpm.project import project_create
from bpm.env import env_create

### bpm create ...
create_parser = bpm_subparsers.add_parser('create')
create_subparsers = create_parser.add_subparsers()

### bpm create project [-n|--name=<project_name>]
create_project_parser = create_subparsers.add_parser('project')
create_project_parser.set_defaults(fn=project_create)
create_project_parser.add_argument('-n', '--name', default='brubeck_project/')

### bpm create env [-f|--file=<file>]
create_env_parser = create_subparsers.add_parser('env')
create_env_parser.set_defaults(fn=env_create)
create_env_parser.add_argument('-f', '--file', default=None)


