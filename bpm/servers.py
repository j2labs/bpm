import os
import fnmatch
import sqlite3
import subprocess
import uuid


def install_mongrel2():
    pass


def find_mongrel2_conf(project_path):
    """Given a Brubeck project directory, attempts to locate a Mongrel2
    configuration file. Returns None if no mongrel2.conf file is found."""

    for root, dirs, files in os.walk(project_path):
        if 'mongrel2.conf' in files:
            return os.path.join(root, 'mongrel2.conf')


def find_mongrel2_db(project_path, create=False):
    """Given a Brubeck project directory, performs a breadth-first search for a
    sqlite database whose schema appears to match that of a Mongrel2
    configuration file."""

    dbs = []
    for root, dirs, files in os.walk(project_path):
        dbs.extend([os.path.join(root, f)
                    for f in fnmatch.filter(files, '*.sqlite')])

    if not dbs and create:
        conf_file = find_mongrel2_conf(project_path)
        if conf_file:
            return generate_mongrel2_db(conf_file)
        else:
            return None

    query = "select name from sqlite_master where type = 'table';"
    expected_tables = set((u'server', u'proxy', u'mimetype', u'statistic',
                           u'setting', u'route', u'log', u'host', u'directory',
                           u'handler'))

    for db in dbs:
        with sqlite3.Connection(db) as con:
            tables = set(row[0] for row in con.execute(query))
        if tables == expected_tables:
            return db


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
