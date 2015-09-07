#!/usr/bin/python3

"""
BuffettBot // Bot.py

The main actor in the BuffettBot application.
"""

# MODULES
# | Native
from sys import exit

# | Third-Party
import mysql.connector

# | Custom
from lib.conf import Conf
from lib.src import Source
from lib.oracle import Oracle
from lib.stoc import Stoc
from lib.tle import Tle

# METADATA
__author__ = 'Joshua Carlson-Purcell'
__copyright__ = 'Copyright 2015, CarlsoNet'
__license__ = 'MIT'
__version__ = '1.0.0-alpha'
__maintainer__ = 'Joshua Carlson-Purcell'
__email__ = 'jcarlson@carlso.net'
__status__ = 'Prototype'

# FUNCTIONS
def printSeparator(separatorSize,printToScreen = True):
    """
    Description:
        Prints out a horizontal seperator of varying sizes

    Params:
        separatorSize [INT]: size of separator

    Output:
        NONE
    """

    seperatorSegment = "####################"
    seperator = ''

    for i in range(0,separatorSize):
        seperator += seperatorSegment

    if printToScreen:
        # print separator to console
        print(seperator)
    else:
        # return separator as string
        return seperator

def startOracleEngine():
    """
    Description:
        Starts Oracle engine with all needed params

    Params:
        NONE

    Output:
        Oracle()
            OR
        str
            OR
        None
    """

    orcl = None

    try:
        ## generate sources
        srcList = [
            Source('https://www.carlso.net/')
        ]

        ## start engine
        orcl = Oracle(srcList)
    except ValueError as e:
        return str(e)

    return orcl

# MAIN
def main():
    printSeparator(3)
    print("BuffettBot v1.0.0-alpha")
    printSeparator(3)

    # PARSE CONF FILES
    conf = Conf({})
    # conf.writeConfData()
    try:
        conf.readConfData()
    except FileNotFoundError:
        print('Conf :: ERROR :: could not load config data!')
        exit(1)

    # START ORACLE ENGINE
    printSeparator(2)
    print("Starting the Oracle...")
    oracle = startOracleEngine()
    if oracle is None:
        print('Oracle :: ERROR :: catastrophic error encountered, please verify Python install and version')
        exit(1)
    elif isinstance(oracle, str):
        print('Oracle :: ERROR :: ' + oracle)
        exit(1)
    else:
        print('Oracle engine started successfully!')
    printSeparator(2)

    # START STOC ENGINE
    printSeparator(2)
    print('Starting STOC...')
    try:
        stoc = Stoc(False)

        print('STOC engine started successfully!')
    except ValueError as e:
        print('STOC :: ERROR :: ' + str(e))
        exit(1)
    printSeparator(2)

    # START TLE
    printSeparator(2)
    print('Starting Trade-Logic Engine (TLE)...')
    try:
        tle = Tle(1)

        print('TLE started successfully!')
    except ValueError as e:
        print('TLE :: ERROR :: ' + e)
    printSeparator(2)

    # print TLE stats
    printSeparator(2)
    print('TLE Stats')
    printSeparator(1)
    print(tle)
    printSeparator(2)

    # END MAIN
    ## everything went well at this point
    exit(0)

if __name__ == '__main__':
    main()
