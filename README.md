# Brubeck Project Manager

Here are the commands that I think Brubeck should have. Some work has been done
and some of that will be carried over.


## Current Commands

I think Brubeck environments should basically be virtual environments. These
things are handy for managing lots of flexibility in environments, in addition
to isolating our needs from the system.


### Starting a project

    $ bpm project create [-n project_name]

This will create a Project directory called `brubeck_project`, unless you
provide a different name.


### Create an environment

    $ cd <project_name>
    $ bpm env create 
    
In that directory will be `settings`, `static`, `templates` and a directory
named after your project. 

Two hidden directories are also used. One is `.virtualenv` where the python
environment is stored. The other is `.var`, where we find the `logs`, `sock`
and `run`. 

### Activating an environment

    $ cd <project_name>
    $ source bin/bpmenv

At this point it is just virtualenv. Turn it off by typing `deactivate`. By 
default the virtualenv is installed in `project_name/.virtualenv`.


## Future Commands

To start Brubeck, use the `up` command. I think this command should probably use
procer to watch over the Python processes.

    $ bpm up
    
To start n Brubeck instances, pass a number to `up`:

    $ bpm up 4

This command will start any relevant web servers and probably also sit on top
of supervisord or procer to keep the processes up until you tell them to stop.
