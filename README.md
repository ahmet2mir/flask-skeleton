# Flask Skeleton with Bootstrap

This is a simple flask skeleton to quickly start a new web project using:

- Bootstrap
- SCSS
- console and rotating file logging
- HTTP basic auth
- web and api views with Blueprint

## Installation

Run:
    make install

With `docker`:

    docker build -t flask-skeleton .

## Usage

Run:

    make server

With `docker`:

    docker run -p 5000:5000 flask-skeleton

With `heroku`:

    heroku create
    git push heroku master
    heroku ps:scale web=1
    heroku open
    heroku logs --tail


## Test

Visit:
    
    http://127.0.0.1:5000/

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
- Log file is in root repo named skeleton.log
- HTTP auth is done by `auth.py`
