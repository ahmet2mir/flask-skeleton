# -*- coding: utf-8 -*-
from __future__ import absolute_import

import logging

from flask import Blueprint, render_template, request, jsonify

from skeleton import controllers
from skeleton.auth import auth

web = Blueprint("web", __name__)
logger = logging.getLogger(__name__)

@web.route('/', methods=['GET'])
@auth.login_required
def index():
    logger.debug("index requested")
    if request.method == "GET":
        return render_template('index.html',
                               something=controllers.something())

