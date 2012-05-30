# Brubeck Project Manager

Here are the commands that I think Brubeck should have. Some work has been done
and some of that will be carried over.


## Environments

I think Brubeck environments should basically be virtual environments. These
things are handy for managing lots of flexibility in environments, in addition
to isolating our needs from the system.

Create a new Brubeck environment:

    $ bpm new_env <env_name>
    
To start a project: 

    $ bpm new_project <project_name>
    
In that directory will be `etc`, `log`, `static`, `run`, `templates` and a
directory named after the environment for your Python code.

To start Brubeck, use the `up` command. I think this command should probably use
procer to watch over the Python processes.

    $ bpm up
    
To start n Brubeck instances, pass a number to `up`:

    $ bpm up 4

`cd` to the logs directory.

    $ bpm cdlogs

Follow the logs for Mongrel2.

    $ bpm tailm2

Follow the logs or Brubeck.

    $ bpm tailbrubeck

[Kracekumar](http://twitter.com/kracetheking) suggests using gevent with pip
for downloading packages in parallel.

    
## Mongrel2

Mongrel2's existence will be somewhat hidden behind bpm. So will Brubeck's,
except for the simple fact of implementing our website in it.
