# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Blueprint, jsonify

from skeleton.auth import auth

api = Blueprint("api", __name__, url_prefix='/api/v1.0')

@api.route('/health', methods=['GET'])
@auth.login_required
def health():
    data = {
        "health": "Good doctor!"
    }
    return jsonify(data), 200
