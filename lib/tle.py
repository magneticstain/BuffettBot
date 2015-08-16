#!/usr/bin/python3

"""
BuffettBot // TLE.py

The TLE (Trade Logic Engine) is the controller for all actions, including:

* Managing trade rules
* Issuing trades
* Managing other misc. metadata
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

class Tle:
    """
    Class representing all TLE-related functions, including managing trade logic, performing trades, and managing metadata
    """

    def __init__(self, tradeRiskLvl):
        if not self.setTradeRiskLevel(tradeRiskLvl):
            raise ValueError('invalid data supplied to TLE!')

    # SETTERS
    def setTradeRiskLevel(self, tradeRiskLvl):
        """
        Description:
            Setter used for setting the risk level or stock trades to make

        Params:
            tradeRiskLvl [INT]: index of risk the operator is willing to take
                0 = least risk :: 10 = most risk

        Output:
            Bool
        """

        # set scale settings
        tradeRiskLvlScaleMin = 0
        tradeRiskLvlScaleMax = 10

        if tradeRiskLvlScaleMin <= tradeRiskLvl and tradeRiskLvlScaleMax <= 10:
            # trade level is valid and within scale range
            self.tradeRiskLvl = tradeRiskLvl

            return True

        return False

    # GETTERS
