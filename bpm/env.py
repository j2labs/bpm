import os
import sys
import shutil
from itertools import chain
import subprocess
import tempfile


from bpm.project import load_settings
from bpm.text import (q_webserver, q_concurrency, q_template_engines,
                      dep_statement_m2)
from bpm.system import run_as_script, install_mongrel2


###
### Constants (choices)
###

ENV_NONE = 'none'
ENV_WSGI = 'wsgi'
ENV_M2 = 'm2'
ENV_GEVENT = 'gevent'
ENV_EVENTLET = 'eventlet'
ENV_JINJA2 = 'jinja2'
ENV_MAKO = 'mako'
ENV_TORNADO = 'tornado'
ENV_MUSTACHE = 'mustache'


###
### Python Environment functions
###

def _ask_a_question(question, choices, accumulate=False, allow_none=False):
    """Asks a `question` and retrives the answer. It then validates the answer
    by matching it against a list of acceptable `choices`. The first answer in
    the choics list will be used as the default.

    If `accumulate` is set to True, the received answer will be split into a
    list, delimited by spaces.

    If `allow_none` is set to True and the string "none" is fond in the
    answers, None is returned. It is otherwise ignored, unless it is in the
    `choices` list.
    """
    ### Ask user for input
    raw_answer = raw_input(question)
    raw_answer = raw_answer.strip()
    raw_answer = raw_answer.lower()

    ### Response for inputs that don't make sense
    error_msg = 'ERROR: That answer makes no sense - %s'

    ### Set default for return value
    answer = choices[0]
    if accumulate:
        answer = list()

    ### Loop across choices, inspecting match and building an answer
    for ra in raw_answer.split(' '):
        ### "none": return None and stops iteration
        if allow_none and ra == ENV_NONE:
            ### accumulate aes into the list. short circuit on none.
            answer = None
            break
        ### accumulate + match: treat `answer` as list and append
        if accumulate and ra in choices:
            answer.append(ra)
        ### match: answer is whatever matched. short circuit on match.
        elif ra in choices:
            answer = ra
            break
        ### Misunderstood answers blow up process
        else:
            raise Exception(error_msg % ra)

    return answer


def ask_webserver(settings):
    ### Default to Mongrel2
    choices = (ENV_M2, ENV_WSGI)
    choice = _ask_a_question(q_webserver, choices)
    if choice == ENV_M2:
        install_mongrel2(settings)
    return choice


def ask_concurrency(settings):
    ### Default to Gevent
    choices = (ENV_GEVENT, ENV_EVENTLET)
    choice = _ask_a_question(q_concurrency, choices)
    return choice


def ask_template_engines(settings):
    ### Default to Jinja2
    choices = (ENV_JINJA2, ENV_MAKO, ENV_TORNADO, ENV_MUSTACHE)
    choice = _ask_a_question(q_template_engines, choices,
                              accumulate=True, allow_none=True)
    return choice
    


def env_create(args):
    import virtualenv

    settings = load_settings()
    
    ### Create virtualenv
    virtualenv.create_environment(settings.dir_virtualenv)
    py_reqs = ['brubeck', 'dictshield', 'ujson']

    ### Ask about preferences
    web_server = ask_webserver(settings)
        
    concurrency = ask_concurrency(settings)
    py_reqs.append(concurrency)
    if concurrency == ENV_GEVENT:
        py_reqs.append('cython')
    
    template_engines = ask_template_engines(settings)
    py_reqs = py_reqs + template_engines

    ### pip install requirements
    pip = os.path.join(settings.dir_virtualenv, 'bin/pip')
    cmd = [pip, 'install', '-I']
    return subprocess.check_call(cmd + py_reqs)

