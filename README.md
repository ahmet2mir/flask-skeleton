# Flask Skeleton with Bootstrap

This is a simple flask skeleton to quickly start a new web project using:

- Bootstrap
- SCSS
- console and rotating file logging
- HTTP basic auth
- web and api views with Blueprint

You can use it:

- localy with autoreload
- dockerized with autoreload
- heroku without autoreload

And you can switch between them.

If you're not confortable with Flask follow:

- [Getting stared](http://flask.pocoo.org/docs/0.10/quickstart/)
- [Model-View-Controller (MVC) Explained -- With Legos](https://realpython.com/blog/python/the-model-view-controller-mvc-paradigm-summarized-with-legos/)
- [Modular Applications with Blueprints](http://flask.pocoo.org/docs/0.10/blueprints/)
- [How to structure large flask applications](https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications)
- [How To Serve Flask Applications with Gunicorn and Nginx on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-14-04)

If you're not confortable with SASS/SCSS follow:

- [Getting Started with SASS (with interactive examples)](https://scotch.io/tutorials/getting-started-with-sass)

## Usage

To lazy people like me, you can simply use make commands to deploy a new project.

**make creates a .deployed file, if you remove it, next time you run make, it will remove your git environment**

clone repository to a project name (important):

    git clone https://github.com/ahmet2mir/flask-skeleton.git myproject
    cd myproject

help message:

    $ make || make usage
    Tools to create a Flask environment.

    When you clone this project, clone into your project name.
    Because *make will rename all 'skeleton' modules and params with this name.
    Default is 'flaskskeleton'.

        example: git clone https://github.com/ahmet2mir/flask-skeleton.git myproject
                    cd myproject
                    make local

    Allowed targets:

        usage: this help.

        local: create virtualenv, install requirements and run.
            auto-reload: yes.
            ctrl+c: stop process.
            next make local: start main.py.

        docker: build image and run.
            auto-reload: yes.
            ctrl+c: remove container.
            next make docker: start container.

        heroku: create, push, scale and run application.
            auto-reload: no, need to push content.
            ctrl+c: stop log tail but application still running.
            next make herok: start web, show info and tail logs.

    /!\ .deployed is a state file, if you remove it, the next time  you will run make, it will remove your git environment.


**start** `locally`:

    make local
    ...
    * Debugger is active!
    * Debugger pin code: 298-561-187


**start** with `docker`:

    make docker
    ...
    * Debugger is active!
    * Debugger pin code: 298-561-187


**start** with `heroku`:

    make heroku
    2015-12-19T11:43:15.165081+00:00 app[web.1]: [2015-12-19 11:43:15 +0000] [3] [INFO] Starting gunicorn 19.4.1
    2015-12-19T11:43:15.212135+00:00 app[web.1]: [2015-12-19 11:43:15 +0000] [11] [INFO] Booting worker with pid: 11


**to stop** press `ctrl+c`
- local: stop process.
- docker: remove container.
- heroku: stop log tail but application still running.

**Next time** you use make with target:
- `make local`: start main.py.
- `make docker`: start container.
- `make heroku`: start web, show info and tail logs.

You can, switch between targets without recreating a new project.

Example:

    $ make local
    ...
    * Debugger is active!
    * Debugger pin code: 298-561-187

    ctrl+c
    $ make docker
    ...
    * Debugger is active!
    * Debugger pin code: 298-561-187

    ctrl+c

    $ make heroku
    ...

## Test

Visit:
    
    http://127.0.0.1:5000/

or get url with heroku:

    $ heroku info -s | grep -i web-url | cut -d'=' -f2
    https://xxxx-yyyy-0000.herokuapp.com/

login: **admin**
password: **mypass**

or

login: **other**
password: **hello**

API:

    curl -XGET -u admin:mypass http://127.0.0.1:5000/api/v1.0/health
    {
      "health": "Good doctor!"
    }

With bad auth:

    curl -XGET -u admin:badpass http://127.0.0.1:5000/api/v1.0/health
    {
      "error": "Unauthorized access"
    }

## Details

- Create new scss files under static/scss/ and make the import in `__main__.scss`, the `main.css` is generated in /static/css/main.css
- Log file is in root repo named myproject.log
- HTTP auth is done by `auth.py`

