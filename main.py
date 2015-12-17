# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask
from flask.ext.assets import Environment, Bundle

# change it
from skeleton.web import web
from skeleton.api import api

import logging
from logging.handlers import RotatingFileHandler

application = Flask(__name__,\
                    static_folder="skeleton/static/",\
                     template_folder="skeleton/templates/",
                    static_url_path="/static")
application.register_blueprint(web)
application.register_blueprint(api)

# Scss
assets = Environment(application)
assets.versions = 'timestamp'
assets.url_expire = True
assets.manifest = 'file:/tmp/manifest.to-be-deployed'  # explict filename
assets.cache = False
assets.auto_build = True

assets.url = application.static_url_path
scss = Bundle('scss/__main__.scss', filters='pyscss', output='css/main.css',  depends=['scss/*.scss'])
assets.register('scss_all', scss)

assets.debug = False
application.config['ASSETS_DEBUG'] = False

# Set Logger
log = logging.getLogger(__name__)
console_formatter = logging.Formatter(
            '%(levelname)s\t%(filename)s:%(lineno)d\t\t%(message)s', '%m-%d %H:%M:%S')
file_formatter = logging.Formatter(
            '%(levelname)s - %(asctime)s - %(pathname)s - l%(lineno)d - %(message)s', '%m-%d %H:%M:%S')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(console_formatter)

rotatingfile_handler = RotatingFileHandler('skeleton.log', maxBytes=10000, backupCount=1)
rotatingfile_handler.setLevel(logging.INFO)
rotatingfile_handler.setFormatter(file_formatter)

log.addHandler(console_handler)
log.addHandler(rotatingfile_handler)
log.setLevel(logging.DEBUG)


def run():
    # Start Application
    log.info("start application")
    application.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == '__main__':
    run()
