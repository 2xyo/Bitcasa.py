#!/bin/env python
# -*- coding: utf-8 -*-

"""Bitcasa.py Client


"""

__author__ = "Yohann Lepage"
__version__ = "0.1"
__email__ = "yohann@lepage.info"
__status__ = "Broken"

import logging
import xmlrpclib
import socket
import sys
import time

try:
    # Python 2
    from xmlrpclib import ServerProxy, ProtocolError
except ImportError:
    # Python 3
    from xmlrpc.client import ServerProxy, ProtocolError


log = logging.getLogger('bitcasa.client')


class BitcasaClient(object):
    """docstring for BitcasaCore"""

    def __init__(self, _username, _password,
                 _address="127.0.0.1", _port=1664):

        self.address = _address
        self.port = _port
        self.username = _username
        self.password = _password 
        
        # try:
        self.server = ServerProxy("http://" + self.address + ":" + str(self.port))
        time.sleep(0.1)
        
        try:
            self.server.ping()
        except:
             log.critical("Connection to the Bitcasa.py server failed !")
             sys.exit()
        else:
            log.debug("Connected to the server")

    def connection(self):
        pass

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
        print self.server.system.listMethods()

    def stopServer(self):
        """
        Yes, it's dirty.
        """
        try:
            return self.server.stop()
        except:
            pass
