###
### Load Modules, including settings modules
###

import os
from settings import constants
from settings.base import *


###
### Prepare Web Server Values
###

if web_server == constants.MONGREL2:
    from settings.mongrel2 import (mongrel2_conf, mongrel2_db,
                                   mongrel2_send_spec, mongrel2_send_ident,
                                   mongrel2_recv_spec, mongrel2_recv_ident)
    def init_msg_conn():
        from brubeck.connections import Mongrel2Connection
        return Mongrel2Connection(mongrel2_send_spec, mongrel2_recv_spec)
    
    mongrel2_conf = os.path.join(dir_settings, mongrel2_conf)
    mongrel2_db = os.path.join(dir_settings, mongrel2_db)
    
elif web_server == constants.WSGI:
    def init_msg_conn():
        from brubeck.connections import WSGIConnection
        return WSGIConnection(port=web_port)
    
else:
    raise Exception('ERROR: Unknown webserver setting')


###
### Prepare Database Values
###

def init_db_conn():
    return dict()
