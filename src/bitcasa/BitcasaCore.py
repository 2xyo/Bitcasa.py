#!/bin/env python
# -*- coding: utf-8 -*-

"""Bitcasa.py Core


"""

__author__ = "Yohann Lepage"
__version__ = "0.1"
__email__ = "yohann@lepage.info"
__status__ = "Broken"

import logging
import os
import sys
import subprocess

from BitcasaException import BitcasaMaxConcurrentUpload, BitcasaBadAuth
from utils.utils import which

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

    def ping(self):
        return "pong"




class CasperJS():
    """
    https://github.com/n1k0/casperjs/blob/master/bin/casperjs
    """

    def resolve(self, path):
        if os.path.islink(path):
            path = os.path.join(os.path.dirname(path), os.readlink(path))
            return self.resolve(path)
        return path

    def run(self, script, option=""):
        PHANTOMJS_NATIVE_ARGS = [
            'cookies-file',
            'config',
            'debug',
            'disk-cache',
            'ignore-ssl-errors',
            'load-images',
            'load-plugins',
            'local-storage-path',
            'local-storage-quota',
            'local-to-remote-url-access',
            'max-disk-cache-size',
            'output-encoding',
            'proxy',
            'proxy-auth',
            'proxy-type',
            'remote-debugger-port',
            'remote-debugger-autorun',
            'script-encoding',
            'web-security',
        ]
        CASPER_ARGS = []
        CASPER_PATH = os.path.abspath(os.path.join(which('casperjs'), '..'))
        PHANTOMJS_ARGS = []
        SYS_ARGS = option

        for arg in SYS_ARGS:
            found = False
            for native in PHANTOMJS_NATIVE_ARGS:
                if arg.startswith('--%s' % native):
                    PHANTOMJS_ARGS.append(arg)
                    found = True
            if not found:
                CASPER_ARGS.append(arg)

        CASPER_COMMAND = os.environ.get('PHANTOMJS_EXECUTABLE', 'phantomjs').split(' ')
        CASPER_COMMAND.extend(PHANTOMJS_ARGS)
        CASPER_COMMAND.extend([
            os.path.join(CASPER_PATH, 'bin', 'bootstrap.js'),
            '--casper-path=%s' % CASPER_PATH,
            '--cli'
        ])
        CASPER_COMMAND.extend(CASPER_ARGS)
        
        script_path = os.path.dirname(self.resolve(__file__))
        script_cmd = os.path.join(script_path, 'js', script)
        CASPER_COMMAND.extend([script_cmd])

        print CASPER_COMMAND[0]
        print CASPER_COMMAND
        process = subprocess.Popen(CASPER_COMMAND, shell=False,
                                   stdout=subprocess.PIPE, 
                                   stderr=subprocess.PIPE)

        # wait for the process to terminate
        self.out, self.err = process.communicate()
        self.errcode = process.returncode

        return self.out, self.err, self.errcode
