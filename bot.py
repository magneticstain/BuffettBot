#!/usr/bin/python3

"""
BuffettBot // Bot.py

The main actor in the BuffettBot application.
"""

# MODULES
# | Native
import sys

# | Third-Party

# | Custom
from lib.oracle import Oracle

# METADATA
__author__ = 'Joshua Carlson-Purcell'
__copyright__ = 'Copyright 2015, CarlsoNet'
__license__ = 'MIT'
__version__ = '1.0.0-alpha'
__maintainer__ = 'Joshua Carlson-Purcell'
__email__ = 'jcarlson@carlso.net'
__status__ = 'Prototype'

# FUNCTIONS

# MAIN
def main():
    print("########################################")
    print("BuffettBot v1.0.0-alpha")
    print("########################################")

    # start Oracle
    print("Starting the Oracle...")
    srcList = [

    ]
    orcl = Oracle(srcList)

if __name__ == '__main__':
    main()
