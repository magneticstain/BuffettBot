#!/usr/bin/python3

"""
BuffettBot // Src.py

An object representing a source, local or third-party, that an Oracle can gather info from
"""

# MODULES
# | Native

# | Third-Party
from re import compile, search, IGNORECASE

# | Custom


# METADATA
__author__ = 'Joshua Carlson-Purcell'
__copyright__ = 'Copyright 2015, CarlsoNet'
__license__ = 'MIT'
__version__ = '1.0.0-alpha'
__maintainer__ = 'Joshua Carlson-Purcell'
__email__ = 'jcarlson@carlso.net'
__status__ = 'Prototype'

class Source:
    """
    A representation of a data source, normally used by Oracle()
    """

    def __init__(self, url):
        if not self.setUrl(url):
            raise ValueError('invalid data supplied for Oracle data source!')

    # SETTERS
    def setUrl(self, url):
        """
        Description:
            Verifies and sets or rejects new data source URL

        Params:
            * URL
                * url of data source

        Output:
            * bool
        """

        # set validation regex
        # based off of Django's URL validator
        urlRegex = compile(
            r'^(?:http)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$',IGNORECASE
        )

        if search(urlRegex, url):
            self.url = url

            return True

        return False

