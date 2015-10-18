#!/usr/bin/python3

"""
BuffettBot

A collection of logic for reading and setting config values
"""

# MODULES
# | Native
from json import dump, load

# | Third-Party

# | Custom


# METADATA
__author__ = 'Joshua Carlson-Purcell'
__copyright__ = 'Copyright 2015, CarlsoNet'
__license__ = 'MIT'
__version__ = '1.0.0-alpha'
__maintainer__ = 'Joshua Carlson-Purcell'
__email__ = 'jcarlson@carlso.net'
__status__ = 'Prototype'

class Conf:
    """
    A class used for handling config values
    """

    def __init__(self, confData = {}):
        if not self.setConfData(confData):
            raise ValueError('invalid data supplied to Conf engine!')

    # SETTERS
    def setConfData(self, confData):
        """
        Description:
            Set dictionary with config data

        Params:
            confData [DICT]: a dictionary filled with config file and related metadata

        Output:
            Bool
        """

        if isinstance(confData, dict):
            # config data is good
            self.confData = confData

            return True

        return False

    # GETTERS
    def getConfData(self):
        """
        Description:
            Returns config data

        Params:
            NONE

        Output:
            Dict
        """

        return self.confData

    # OTHER FUNCTIONS
    def readConfData(self, confFile = './conf/main.json'):
        """
        Description:
            Reads in config data saved in JSON format

        Params:
            confFile [STR]: filename of config file to parse

        Output:
            Dict
        """

        # open file
        confFileHandle = open(confFile)

        # parse json contents
        confJsonDict = load(confFileHandle)

        # close handle
        confFileHandle.close()

        self.confData = confJsonDict

    def writeConfData(self, confFile = './conf/main.json'):
        """
        Description:
            Writes config data to file in JSON format

        Params:
            confFile [STR]: filename of where to save data to

        Output:
            NONE
        """

        # open file
        confFileHandle = open(confFile, 'w')

        # write out config data in JSON format
        dump(self.confData, confFileHandle)

        # close file handle
        confFileHandle.close()

    def __str__(self):
        """
        Description:
            Overload of magic method to output a string when class is treated as such

        Params:
            NONE

        Output:
            STR
        """

        configDataStr = 'CONFIG DATA: ' + str(self.confData)

        return configDataStr