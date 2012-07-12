import os
import shutil
import imp
import subprocess
from itertools import chain


from bpm.text import dep_statement_bpm
from bpm.system import walk_up_until, import_dir


###
### Project Organization
###

def find_settings():
    """This function attempts to discover the full path to a Brubeck project's
    settings file.
    """
    root_path = os.getcwd()
    path = walk_up_until(root_path, 'settings/')
    if path:
        return path

def load_settings():
    """Simple function that finds the settings file and returns a loaded python
    module.
    """
    settings_path = find_settings()
    settings = import_dir(settings_path)
    return settings


###
### Project Manipulation Functions
###

def find_skel_dir(root_path):
    """Walks up from root_path, looking for a directory that matches the
    expected bpm skeleton directory path.
    """
    root_path = os.path.dirname(os.path.abspath(__file__))
    return walk_up_until(root_path, 'share/bpm/skel')


def _rename_project(project_path, new_name):
    """Rename project dir in skel after project
    """
    ### Rename directory
    before = project_path + '/project'
    after = project_path + '/' + new_name
    shutil.move(before, after)

    ### Replace occurrences

    
def install_with_pip(py_reqs):
    """Simple function for installing python packages with the virtualenv's
    pip.
    """
    settings = load_settings()
    pip = os.path.join(settings.dir_virtualenv, 'bin/pip')
    cmd = [pip, 'install', '-I']
    return subprocess.check_call(cmd + py_reqs)    


def project_create(args):
    """Implements the `create` command. It essentially copies the contents of
    `bpm/settings/skel/` into a directory to bootstrap a project's design.
    """
    try:
        import pip
        import virtualenv
    except:
        response = raw_input(dep_statement_bpm)
    
    ### Find path to skel dir
    bpm_path = os.path.dirname(os.path.abspath(__file__))
    skel_path = find_skel_dir(bpm_path)

    if not skel_path:
        raise Exception("No project skeleton directory found!")

    ### Check validity of project name
    cwd = os.getcwd()
    project_path = '/'.join([cwd, args.name])
    if os.path.exists(project_path):
        error_msg = "Project directory %s already exists.  Please remove " \
                    "before continuing." % project_path
        raise ValueError(error_msg)

    ### Copy skel over
    shutil.copytree(skel_path, project_path)

    ### Rename project dir in skel after project
    _rename_project(project_path, args.name)
