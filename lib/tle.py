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

class Tle:
    """
    Class representing all TLE-related functions, including managing trade logic, querying trades, and managing metadata
    """

    def __init__(self, tradeRiskLvl = 1, balance = 0, moneySpent = 0, profit = 0):
        if (
                not self.setBalance(balance)
                or not self.setMoneySpent(moneySpent)
                or not self.setProfit(profit)
                or not self.setTradeRiskLevel(tradeRiskLvl)
        ):
            raise ValueError('invalid data supplied to TLE!')

    # SETTERS
    def setBalance(self, balance):
        """
        Description:
            Sets current available balance to be used for trade

        Params:
            balance (INT): new available balance value

        Output:
            Bool
        """

        # balance can be any integer
        self.balance = balance

        return True


    def setMoneySpent(self, moneySpent):
        """
        Description:
            Sets current amount of money spent so far

        Params:
            balance (INT): new amount of money spent

        Output:
            Bool
        """

        # moneySpent can be any integer
        self.moneySpent = moneySpent

        return True


    def setProfit(self, profit):
        """
        Description:
            Sets current amount of profit made from trades

        Params:
            profit (INT): new profit amount

        Output:
            Bool
        """

        # profit can be any integer
        self.profit = profit

        return True

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
    def getBalance(self):
        """
        Description:
            Returns current balance

        Params:
            NONE

        Output:
            Int
        """

        return self.balance

    def getMoneySpent(self):
        """
        Description:
            Returns current amount of money spent on trades

        Params:
            NONE

        Output:
            Int
        """

        return self.moneySpent

    def getProfit(self):
        """
        Description:
            Returns current amount of profit made

        Params:
            NONE

        Output:
            Int
        """

        return self.profit

    def getTradeRiskLevel(self):
        """
        Description:
            Returns trade risk level

        Params:
            NONE

        Output:
            Int
        """

        return self.tradeRiskLvl

    # OTHER FUNCTIONS
    def getMetadataFromDb(self):
        """
        Description:
            Query database for metadata (balance, profit, etc)

        Params:
            None

        Output:
            Bool
        """



    def __str__(self):
        """
        Description:
            Overload of magic method to output a string when class is treated as such

        Params:
            NONE

        Output:
            Str
        """

        # generate stats string
        stats = (
                    'Current Balance: $' + str(self.balance) + '\n' +
                    'Total Money Spent: $' + str(self.moneySpent) + '\n' +
                    'Overall Profit: $' + str(self.profit) + '\n' +
                    'Current Trade Risk Level [1-10]: ' + str(self.tradeRiskLvl)
        )

        return stats