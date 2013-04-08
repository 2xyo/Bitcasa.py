#!/bin/env python
# -*- coding: utf-8 -*-

"""Bitcasa Core


"""

from BitcasaException import BitcasaMaxConcurrentUpload, BitcasaBadAuth

__author__ = "Yohann Lepage"
__version__ = "0.1"
__email__ = "yohann@lepage.info"
__status__ = "Broken"



class BitcasaCore(object):
    """docstring for BitcasaCore"""

    def __init__(self, arg):
        super(BitcasaCore, self).__init__()
        self.arg = arg
    
    def login():
        raise NotImplementedError

    def uploadUrl():
        raise NotImplementedError
    
    def uploadAllUrl():
        raise NotImplementedError

    def uploadFile():
        raise NotImplementedError

    def uploadDir():
        raise NotImplementedError

    def uploadList():
        raise NotImplementedError

    def status():
        raise NotImplementedError

    def search():
        raise NotImplementedError