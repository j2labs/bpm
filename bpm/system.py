import sys

from bpm.mongrel2 import (get_mongrel2_status, mongrel2_reload, mongrel2_load,
                          mongrel2_start, mongrel2_stop, mongrel2_log)


def system_run(args):
    import settings
    if settings.APP_DIR not in sys.path:
        sys.path.insert(0, settings.APP_DIR)

    # signal.signal(signal.SIGINT, lambda signal, frame: True)
    mod = __import__(args.app_name)
    mod.app.run()


def system_status(args):
    import settings
    status, msg = get_mongrel2_status(settings.MONGREL2_DB, args.host)
    print msg


def system_load(args):
    import settings
    mongrel2_load(settings.MONGREL2_DB, args.conf_file)


def system_start(args):
    import settings
    mongrel2_start(settings.MONGREL2_DB, args.host, not args.foreground)


def system_stop(args):
    import settings
    mongrel2_stop(settings.MONGREL2_DB, args.host)


def system_log(args):
    import settings
    mongrel2_log(settings.MONGREL2_DB, args.host)


def system_reload(args):
    import settings
    mongrel2_reload(settings.MONGREL2_DB, args.host)
