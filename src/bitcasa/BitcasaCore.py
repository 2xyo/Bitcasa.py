#!/bin/env python
# -*- coding: utf-8 -*-

"""Bitcasa.py Core


"""

__author__ = "Yohann Lepage"
__version__ = "0.1"
__email__ = "yohann@lepage.info"
__status__ = "Broken"

import logging
from BitcasaException import BitcasaMaxConcurrentUpload, BitcasaBadAuth

log = logging.getLogger('bitcasa.core')

class Bitcasa(object):
    """docstring for BitcasaCore"""

    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def login(self):
        raise NotImplementedError

    def uploadUrl(self):
        raise NotImplementedError
    
    def uploadAllUrl(self):
        raise NotImplementedError

    def uploadFile(self):
        raise NotImplementedError

    def uploadDir(self):
        raise NotImplementedError

    def uploadList(self):
        raise NotImplementedError

    def status(self):
        raise NotImplementedError

    def search(self):
        raise NotImplementedError

    def hello(self):
        log.info('hello')
        return "Hello"
