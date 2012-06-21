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


