#!/usr/bin/python3

"""
BuffettBot // Bot.py

The main actor in the BuffettBot application.
"""

# MODULES
# | Native
from sys import exit

# | Third-Party

# | Custom
from lib.oracle import Oracle
from lib.src import Source

# METADATA
__author__ = 'Joshua Carlson-Purcell'
__copyright__ = 'Copyright 2015, CarlsoNet'
__license__ = 'MIT'
__version__ = '1.0.0-alpha'
__maintainer__ = 'Joshua Carlson-Purcell'
__email__ = 'jcarlson@carlso.net'
__status__ = 'Prototype'

# FUNCTIONS
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
            # Source('https://ww')
        ]

        ## start engine
        orcl = Oracle(srcList)
    except ValueError as e:
        return str(e)

    return orcl

# MAIN
def main():
    print("########################################")
    print("BuffettBot v1.0.0-alpha")
    print("########################################")

    # START ORACLE ENGINE
    print("Starting the Oracle...")
    oracle = startOracleEngine()
    if oracle is None:
        print('ERROR: catastrophic error encountered, please verify Python install and version')
        exit(1)
    elif isinstance(oracle, str):
        print('ERROR: ' + oracle)
        exit(1)
    else:
        print('Oracle engine started successfully!')

    # END MAIN
    ## everything went well if at this point
    exit(0)

if __name__ == '__main__':
    main()
