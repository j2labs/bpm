import os
import shutil
from itertools import chain
import imp

from bpm.text import dep_statement_bpm


def _walk_up_until(root_path, sub_path):
    """Starts at `root_path` and basically loops through `cd ..` until it finds
    a directory that contains `sub_path`, or it reaches root.

    It returns the directory that had `sub_path` in it on success and returns
    None if nothing is found.
    """
    cur_dir = root_path
    while cur_dir != '/':
        potential_path = os.path.join(cur_dir, sub_path)
        if os.path.exists(potential_path):
            return potential_path
        cur_dir = os.path.dirname(cur_dir)
    return None


def load_settings():
    """This function attempts to discover the full path to a Brubeck project's
    settings file.
    """
    root_path = os.getcwd()
    ### Load settings/base.py, but import as just settings
    path = _walk_up_until(root_path, 'settings/base.py')
    if path:
        return imp.load_source('settings', path)


def find_skel_dir(root_path):
    """Walks up from root_path, looking for a directory that matches the
    expected bpm skeleton directory path.
    """
    root_path = os.path.dirname(os.path.abspath(__file__))
    return _walk_up_until(root_path, 'share/bpm/skel')
        

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
    before = project_path + '/project'
    after = project_path + '/' + args.name
    shutil.move(before, after)
