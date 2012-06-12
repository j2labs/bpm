###
### User Questions
###

q_webserver = """
# Web Server

Choices:
  m2*:  http://mongrel2.org
  wsgi: http://wsgi.readthedocs.org
    
Choose one (m2 wsgi):
"""
    

q_concurrency = """
# Concurrency

Choices:
  gevent*:  http://gevent.org
  eventlet: http://eventlet.net

Choose one (gevent eventlet):
"""

q_template_engines = """
# Templating

Choices:
  jinja2*:  http://jinja.pocoo.org/
  mako:     http://www.makotemplates.org/
  tornado:  http://www.tornadoweb.org/documentation/template.html
  mustache: http://mustache.github.com/
    
Choose one or more (jinja2 mako tornado mustache none):
"""


###
### Dependency Statements
###

dep_statement_bpm = """
# BPM dependencies

BPM needs pip and virtualenv

    Ubuntu: sudo apt-get install python-pip python-virtualenv
    Mac:    sudo easy_install pip && sudo pip install virtualenv

Press enter when finished.
"""

dep_statement_m2 = """
# Mongrel2 dependencies

Mongrel2 requires: zeromq, sqlite3 and libuuid. 

Ubuntu: sudo apt-get install libevent-dev sqlite3 libsqlite3-dev uuid-dev python-dev
Mac:    brew install libevent sqlite3

ZeroMQ is installed manually. Press enter when finished.
"""


###
### Install From Source
###

installer_zeromq = """
wget http://download.zeromq.org/zeromq-2.2.0.tar.gz
tar zxf zeromq-2.2.0.tar.gz
cd zeromq-2.2.0
./configure --prefix=$PWD/../..
make
make install
cd ..
"""


installer_mongrel2 = """
wget http://mongrel2.org/static/downloads/mongrel2-1.7.5.tar.bz2
tar jxf mongrel2-1.7.5.tar.bz2
cd mongrel2-1.7.5/
env OPTFLAGS="-I$PWD/../../include" OPTLIBS="-L$PWD/../../lib" LD_RUN_PATH=$PWD/../../lib make
env OPTFLAGS="-I$PWD/../../include" OPTLIBS="-L$PWD/../../lib" LD_RUN_PATH=$PWD/../../lib PREFIX=$PWD/../.. make install
cd ..
"""


installer_pyzmq = """
git clone https://github.com/zeromq/pyzmq.git
cd pyzmq
git checkout v2.2.0
../../bin/python ./setup.py install --zmq=$PWD/../../
cd ..
"""


installer_gevent_zeromq = """
git clone https://github.com/traviscline/gevent-zeromq.git
cd gevent-zeromq
git checkout v0.2.2
../../bin/python ./setup.py install 
cd ..
"""
