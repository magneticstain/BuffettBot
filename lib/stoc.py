#!/usr/bin/python3

"""
BuffettBot // STOC.py

STOC (Securities and Trade Operation Controller) is the engine responsible for issuing, verifying, and gathering trades made to the trading API(s)
"""

# MODULES
# | Native

# | Third-Party
import mysql.connector

# | Custom


# METADATA
__author__ = 'Joshua Carlson-Purcell'
__copyright__ = 'Copyright 2015, CarlsoNet'
__license__ = 'MIT'
__version__ = '1.0.0-alpha'
__maintainer__ = 'Joshua Carlson-Purcell'
__email__ = 'jcarlson@carlso.net'
__status__ = 'Prototype'

class Stoc:
    """
    Class for trade-initiation logic, including: issuing trades, verifying trades, and gathering results-based trade data
    """

    def __init__(self, status):
        if not self.setStatus(status):
            raise ValueError('invalid data supplied to STOC engine!')

    # SETTERS
    def setStatus(self, status):
        """
        Description:

        Params:
            status [BOOL]: setting [0 or 1, off or on] for engine status

        Output:
            Bool
        """

        if isinstance(status, bool):
            # param is good
            self.status = status

            return True

    #GETTERS
    def getStatus(self):
        """
        Description:
            Returns current engine status

        Params:
            NONE

        Output:
            Bool
        """

        return self.status