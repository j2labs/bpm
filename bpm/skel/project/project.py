#!/usr/bin/env python


from brubeck.request_handling import Brubeck
from brubeck.connections import Mongrel2Connection

from settings import init_db_conn, init_msg_conn, log_level, cookie_secret
from {{BPM_PROJECT_NAME}}.handlers import TakeFiveHandler


### Instantiate connections
db_conn = init_db_conn()
msg_conn = init_msg_conn()


### Routes
handler_tuples = [
    (r'^/', TakeFiveHandler),
]


### App config
app_config = {
    'msg_conn': msg_conn,
    'handler_tuples': handler_tuples,
    'db_conn': db_conn,
    'cookie_secret': cookie_secret,
    'log_level': log_level,
}


### Instances
app = Brubeck(**app_config)
app.run()
