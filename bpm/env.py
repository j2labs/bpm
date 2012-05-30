import os
import sys
import shutil
from itertools import chain
import virtualenv
import pip
import subprocess


from bpm.project import load_settings


def env_create(args):
    settings = load_settings()
    
    ### Create virtualenv
    virtualenv.create_environment(settings.dir_virtualenv)
    reqs = ['brubeck', 'dictshield', 'ujson']

    ### Ask about WSGI / Mongrel2, default to WSGI
    print 'args:', args

    ### Ask about Template rendering, default to Jinja2

    ### Ask about concurrency, default to gevent
    concurrency = 'gevent'
    reqs.append(concurrency)

    ### pip install requirements
    
    
    pip = os.path.join(settings.dir_virtualenv, 'bin/pip')
    cmd = [pip, 'install', '-I']
    return subprocess.check_call(cmd + reqs)

