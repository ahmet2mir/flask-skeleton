# -*- coding: utf-8 -*-
from __future__ import absolute_import

import logging

from flask import make_response, jsonify
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
logger = logging.getLogger(__name__)

allowed_users = {
    "admin": {
        "password": "mypass"
    },
    "other": {
        "password": "hello"
    }
}

@auth.get_password
def get_password(username):
    logger.debug("request from {0}".format(username))
    if username in allowed_users:
        return allowed_users[username]["password"]
    return

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)
