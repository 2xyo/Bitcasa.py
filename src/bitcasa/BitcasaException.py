#!/bin/env python
# -*- coding: utf-8 -*-

"""Bitcasa.py Exception


"""

__author__ = "Yohann Lepage"
__version__ = "0.1"
__email__ = "yohann@lepage.info"
__status__ = "Broken"


class BitcasaMaxConcurrentUpload(Exception):
    """Exception raised when we have reach the maximum of 3
    concurrent upload.

    Attributes:
        expr -- input expression in which the error occurred
        msg  -- explanation of the error
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class BitcasaBadAuth(Exception):
    """Exception raised when authentification failed.

    Attributes:
        expr -- input expression in which the error occurred
        msg  -- explanation of the error
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)