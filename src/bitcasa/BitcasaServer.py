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

try:
    # Python 2
    from SimpleXMLRPCServer import SimpleXMLRPCServer
    from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
except ImportError:
    # Python 3
    from xmlrpc.server import SimpleXMLRPCServer
    from xmlrpc.server import SimpleXMLRPCRequestHandler


log = logging.getLogger('bitcasa.server')



class BitcasaHandler(SimpleXMLRPCRequestHandler):
    """
    Main XMLRPC handler
    """
    rpc_paths = ('/RPC2',)


class BitcasaInstance():
    """
    All the methods of this class are published as XML RPC methods
    """

    def __init__(self, username, password):
        self.usernane = username
        self.password = password
        
    def hello(self):
        log.info('hello')

    def start(self):
        log.info('start')

    def ping(self):
        log.debug("ping")
        return True
    
    def deadlock(self):
        pass


class BitcasaServerThread(threading.Thread):

    def __init__(self, *args, **kwargs):

        self.bind_address = "localhost"
        self.bind_port = 45670
        threading.Thread.__init__(self)
        self.timeToQuit = threading.Event()
        self.timeToQuit.clear() 


    def stop(self):
        self.server.server_close()
        self.server = None
        self.timeToQuit.set()
        self.server.server_close()  
        #self.server.deadlock() # dummy call to unlock the socket deadlock

    def run(self):
        log.debug("Start Server Thread")
        self.server = SimpleXMLRPCServer((self.bind_address, self.bind_port),
                                         requestHandler=BitcasaHandler)

        #self.server.register_introspection_functions()
        
        self.server.register_instance(BitcasaInstance("user","pass"))
        

        while not self.timeToQuit.isSet():
            self.server.handle_request()


class BitcasaServer():
    """
    This class creates and manages the TCP Server
    """

    def __init__(self):
        self.server = BitcasaServerThread()


    def start(self):
        log.debug("Start Server")
        self.server.start()
        log.debug("Server started")


    def stop(self):
        log.debug("Stop Server")
        self.server.stop()
        
        log.debug("Server stopped")

