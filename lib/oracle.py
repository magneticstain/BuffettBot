#!/usr/bin/python3

"""
BuffettBot // Oracle.py

The Oracle engine is responsible for gathering third-party data for us in making data-driven decisions.
Along with that, it also created new rules of its own based on previously-learned patterns.
"""

# MODULES
# | Native

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

class Oracle:
    """
    Class for the main data gathering and analyzation engine
    """

    def __init__(self, sourceList):
        if not self.setSources(sourceList):
            raise ValueError('invalid data supplied to the Oracle!')

    # SETTERS
    def setSources(self, sourceList):
        """
        Purpose:
            Sets collection of sources (as objects)

        Params:

        Output:
        """

        # expects an array of source()'s


        return False