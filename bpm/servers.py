import os
import fnmatch
import sqlite3
import subprocess
import uuid

from bpm.system import run_as_script
from bpm.text import (dep_statement_m2,
                      installer_zeromq, installer_mongrel2, installer_pyzmq,
                      installer_gevent_zeromq)


###
### Mongrel2
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


def generate_mongrel2_db(conf_file_path, destination=None):
    """Given the path to a Mongrel2 configuration file, generate a
    configuration database.  If no destination filename is given, the Mongrel2
    configuration database is called config.sqlite and is placed at the same
    directory as the configuration file.  Returns the path of the created
    database."""

    if not destination:
        destination = os.path.join(os.path.dirname(conf_file_path),
                                   'config.sqlite')

    cmd = ['m2sh', 'load', '-config', conf_file_path, '-db', destination]
    subprocess.check_call(cmd)
    return destination


def get_mongrel2_status(conf_db, host):
    """Returns True if Mongrel2 is running.  Returns false otherwise."""
    cmd = ['m2sh', 'running', '-db', conf_db, '-host', host]
    if hasattr(subprocess, 'check_output'):
        response = subprocess.check_output(cmd)
    else:
        response = subprocess.Popen(cmd,
                                    stdout=subprocess.PIPE).communicate()[0]
    status = 'NOT' not in response
    return status, response


def mongrel2_start(conf_db, host, daemonize=True):
    """Starts Mongrel2."""
    cmd = ['m2sh', 'start', '-db', conf_db, '-host', host]
    if daemonize:
        cmd.append('-sudo')

    return subprocess.check_call(cmd)


def mongrel2_stop(conf_db, host):
    """Stops Mongrel2."""
    cmd = ['m2sh', 'stop', '-db', conf_db, '-host', host]
    return subprocess.check_call(cmd)


def mongrel2_reload(conf_db, host):
    """Stops Mongrel2."""
    cmd = ['m2sh', 'reload', '-db', conf_db, '-host', host]
    return subprocess.check_call(cmd)


def mongrel2_load(conf_db, conf_file):
    cmd = ['m2sh', 'load', '-config', conf_file, '-db', conf_db]
    return subprocess.check_call(cmd)


def mongrel2_log(conf_db, host):
    cmd = ['m2sh', 'log', '-db', conf_db, '-host', host]
    return subprocess.check_call(cmd)


def render_mongrel2_conf(port=6767, server_name='brubeck',
                         send_spec='ipc://run/mongrel2_send', send_ident=None,
                         recv_spec='ipc://run/mongrel2_recv', recv_ident='',
                         server_uuid=None):
    """Renders a Mongrel2 configuration using the included Mongrel2 config template.
    """
    send_ident = send_ident or uuid4()
    server_uuid = server_uuid or uuid4()
    return MONGREL_TEMPLATE % locals()
