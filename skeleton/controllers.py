# -*- coding: utf-8 -*-
from __future__ import absolute_import

import logging
logger = logging.getLogger(__name__)

def something():
    logger.debug("do something")
    return "hello world!"