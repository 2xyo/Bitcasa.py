#!/bin/env python
# -*- coding: utf-8 -*-

"""Bitcasa Server


"""

__author__ = "Yohann Lepage"
__version__ = "0.1"
__email__ = "yohann@lepage.info"
__status__ = "Broken"

import logging
import threading
import sys
import atexit
import errno
import time
from socket import error as socket_error

from BitcasaCore import Bitcasa

try:
    # Python 2
    from SimpleXMLRPCServer import SimpleXMLRPCServer
    from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
except ImportError:
    # Python 3
    from xmlrpc.server import SimpleXMLRPCServer
    from xmlrpc.server import SimpleXMLRPCRequestHandler

try:
    # Python 2
    from xmlrpclib import ServerProxy, ProtocolError
except ImportError:
    # Python 3
    from xmlrpc.client import ServerProxy, ProtocolError


log = logging.getLogger('bitcasa.server')



class BitcasaHandler(SimpleXMLRPCRequestHandler):
    """
    Main XMLRPC handler

    Todo: Authentification
    """
    rpc_paths = ('/RPC2',)


class BitcasaInstance():
    """
    All the methods of this class are published as XML RPC methods
    """

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bitcasa = Bitcasa(self.username, self.password)

    def ping(self):
        return self.bitcasa.ping()
    
    def deadlock(self):
        pass


class BitcasaServerThread(threading.Thread):
    """

    """
    def __init__(self, _username, _password,
                    _bind_address="127.0.0.1",
                    _port=1664, *args, **kwargs):

        self.bind_address = _bind_address
        self.bind_port = _port
        self.username = _username
        self.password = _password
        threading.Thread.__init__(self)
        self.timeToQuit = threading.Event()
        self.timeToQuit.clear() 

    #@staticmethod
    def stop(self):
        """
        Hara-Kiri  like a dumbass
        """
        self.server.server_close()
        self.timeToQuit.set()
        sys.exit(1)


    def run(self):
        log.debug("Start Server Thread")
        try:
            self.server = SimpleXMLRPCServer((self.bind_address, self.bind_port),
                                         requestHandler=BitcasaHandler)
        except socket_error as serr:
            if serr.errno != errno.EADDRINUSE:
                  log.critical(serr)
                  sys.exit()
            log.critical("The port is already used (maybe by an old process" 
                        + " of Bitcasa.py, please choose another one.")
            sys.exit(1)
            

        self.server.register_introspection_functions()
        self.server.register_function(self.stop)
        self.server.register_instance(BitcasaInstance(self.username,self.password))
        
        while not self.timeToQuit.isSet():
            self.server.handle_request()

        log.debug("Server thread stopped")


class BitcasaServer():
    """
    This class launches the TCP Server
    """

    def __init__(self, username, password):
        self.server = BitcasaServerThread(username, password)


    def start(self):
        log.debug("Start Server")
        self.server.start()
        time.sleep(0.5)


    def stop(self):
        raise Exception("Server must me stopped by the client.")



#atexit.register(cleanSocket)
