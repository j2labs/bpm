import sys
import tempfile
import subprocess


from bpm.text import (dep_statement_m2,
                      installer_zeromq, installer_mongrel2, installer_pyzmq,
                      installer_gevent_zeromq)


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


###
### Source-based Installers
###

def install_mongrel2(settings):
    """High-level installer for Mongrel2. Includes zeromq, pyzmq and
    gevent_zeromq.
    """
    response = raw_input(dep_statement_m2)
    
    run_as_script(settings, installer_zeromq)
    run_as_script(settings, installer_mongrel2)
    run_as_script(settings, installer_pyzmq)
    run_as_script(settings, installer_gevent_zeromq)
    
