# Brubeck Package Manager

Here are the commands that I think Brubeck should have. Some work has been done
and some of that will be carried over.


## Environments

I think Brubeck environments should basically be virtual environments. These
things are handy for managing lots of flexibility in environments, in addition
to isolating our needs from the system.

Create a new Brubeck environment:

    $ bpm new_env <env_name>
    
In the directory will be `etc`, `log`, `static`, `run`, `templates` and a
directory named after the environment for your Python code.

To start a project: 

    $ bpm new_project <project_name>
    
To start Brubeck:

    $ bpm up
    
To start 4 Brubeck instances:

    $ bpm up 4


## Remote Environments

[Kracekumar](http://twitter.com/kracetheking) suggests using gevent with pip
for downloading packages in parallel.

Perhaps that could look like this:

    $ bpm remote new_env <env_name> --requirements envs/brubeck.reqs

    
## Mongrel2

Mongrel2's existance will be somewhat hidden behind bpm. So will Brubeck's,
except for the simple fact of implementing our website in it.
