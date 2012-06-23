import os
import sys
import tempfile
import subprocess


def run_as_script(settings, script):
    """Takes a settings directory, so it can locate the src directory, and then
    writes `script` to a tmp file, which it then executes.
    """
    src_dir = settings.dir_virtualenv + '/src'
    
    fd, tempname = tempfile.mkstemp()
    f = open(tempname, 'w')
    f.write('mkdir -p %s\n' % (src_dir))
    f.write('cd %s\n' % (src_dir))
    f.write(script)
    f.close()

    cmd = ['sh', tempname]
    return subprocess.check_call(cmd)


def walk_up_until(root_path, sub_path):
    """Starts at `root_path` and basically loops through `cd ..` until it finds
    a directory that contains `sub_path`, or it reaches root.

    It returns the directory that had `sub_path` in it on success and returns
    None if nothing is found.
    """
    cur_dir = root_path
    while cur_dir != os.sep:
        potential_path = os.path.join(cur_dir, sub_path)
        if os.path.exists(potential_path):
            return potential_path
        cur_dir = os.path.dirname(cur_dir)
    return None


def import_dir(full_path_to_module):
    ### Chop off trailing '/' if present
    if full_path_to_module[-1] == os.sep:
        full_path_to_module = full_path_to_module[0:-1]
    module_dir, module_name = os.path.split(full_path_to_module)
    sys.path.insert(0, module_dir)
    module_obj = __import__(module_name)
    module_obj.__file__ = full_path_to_module
    sys.path.remove(module_dir)
    return module_obj


def import_file(full_path_to_module):
    """I don't like doing this, but I don't know of a better way. If you are
    reading this code and have a solution, please send one.

    In the meantime, I must credit this Stack Overflow: http://bit.ly/PPf9y0
    """
    module_dir, module_file = os.path.split(full_path_to_module)
    module_name, module_ext = os.path.splitext(module_file)
    sys.path.insert(0, module_dir)
    module_obj = __import__(module_name)
    module_obj.__file__ = full_path_to_module
    sys.path.remove(module_dir)
    return module_obj
