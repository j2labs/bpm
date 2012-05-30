# Brubeck Project Manager

Here are the commands that I think Brubeck should have. Some work has been done
and some of that will be carried over.


## Environments

I think Brubeck environments should basically be virtual environments. These
things are handy for managing lots of flexibility in environments, in addition
to isolating our needs from the system.

To start a project: 

    $ bpm project create [-n project_name]

Create a new Brubeck environment:

    $ bpm env create 
    
In that directory will be `settings`, `log`, `static`, `run`, `templates` and a
directory named after the environment for your Python code.


## Future Commands

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

