#!/usr/bin/env python


import os
import fnmatch

from distutils.core import setup

skel_paths =  [
    'bpm/skel',
    'bpm/skel/.var',
    'bpm/skel/.var/log',
    'bpm/skel/.var/run',
    'bpm/skel/.var/sock',
    'bpm/skel/bin',
    'bpm/skel/project',
    'bpm/skel/settings',
    'bpm/skel/static',
    'bpm/skel/templates',
]


DATA_EXCLUDE = [
    "*~",
    ".svn*",
    "*.pyc",
    "*.pyo",
]


def get_data_files(data_dir):
    excluded = ["*~", ".svn", "*.pyc", "*.pyo"]
    lst = []

    for file in os.listdir(data_dir):
        exclude = False
        for exc_pattern in excluded:
            if fnmatch.fnmatch(file, exc_pattern) or \
                    os.path.isdir(os.path.join(data_dir, file)):
                exclude = True
                break
        if not exclude:
            lst.append(os.path.join(data_dir, file))
    return lst


my_data_files=[]
for d in skel_paths:
    target_dir = os.path.join("share", d)
    files = get_data_files(d)
    my_data_files.append( (target_dir, files) )


setup(name='bpm',
      version='0.1.1',
      description='Brubeck Project Manager',
      author='James Dennis',
      author_email='jdennis@gmail.com',
      url='http://github.com/j2labs/bpm',
      packages=['bpm'],
      data_files=my_data_files,
      scripts=['bin/bpm', 'bin/bpmrc'])
