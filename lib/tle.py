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
from lib.conf import Conf

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
    def setMetadataToDefault(self, balance = 0, moneySpent = 0, profit = 0, tradeRiskLvl = 1):
        """
        Description:
            set one or more metadata values back to their default value

        Params:
            balance [INT]: default value of balance
            moneySpent [INT]: default value of money spent
            profit [INT]: default value of profit
            tradeRiskLvl [INT]: default value of trade risk level

        Output:
            NONE
        """

        # set object va;s
        self.setBalance(balance)
        self.setMoneySpent(moneySpent)
        self.setProfit(profit)
        self.setTradeRiskLevel(tradeRiskLvl)

    def getMetadataFromDb(self, dbConfData, dataName):
        """
        Description:
            Query database for metadata (balance, profit, etc)

        Params:
            dbConfData [DICT]: the configuration data for the BufferBot database (e.g. username, password, etc)
            dataName [STR]: name of the type of data to query for in the database

        Output:
            BLOB
        """

        dbData = ''

        # connect to db using supplied config data
        dbConn = mysql.connector.connect(**dbConfData)
        cursor = dbConn.cursor()

        # query for metadata
        # set query
        query = "SELECT " \
                "   data_value " \
                "FROM " \
                "   tle.account_metadata " \
                "WHERE " \
                "   data_name = %s"


        # run it
        try:
            # print('DEBUG :: Tle() :: getMetadataFromDb() :: Selecting :: ' + str(dataName))
            cursor.execute(query, (dataName,))
            #dbConn.commit()
            # gather the data
            dbData = cursor.fetchone()[0]
            # print('DEBUG :: Tle() :: getMetadataFromDb() :: Selecting :: DB DATA VAL :: ' + str(dbData))
        except mysql.connector.Error as error:
            # print('DEBUG :: Tle() :: getMetadataFromDb() :: MySQL Error :: ' + str(error.errno) + ' :: ' + error.msg)
            # select failed
            return False

        # close db connection
        dbConn.close()

        if dbData is None:
            # print('DEBUG :: dbData IS NONE')
            return False

        return dbData

    def setMetadataInDb(self, dbConfData, dataName, dataVal):
        """
        Description:
            Sets data for given data name in database

        Params:
            dbConfData [DICT]: the configuration data for the BufferBot database (e.g. username, password, etc)
            dataName [STR]: name of the type of data to query for in the database
            dataVal [BLOB]: data to be set in the database for given dataName

        Output:
            Bool
        """

        # connect to db using supplied config data
        dbConn = mysql.connector.connect(**dbConfData)
        cursor = dbConn.cursor()

        # check if we need to insert a new value or update an old one
        currentDbDataVal = self.getMetadataFromDb(dbConfData, dataName)
        if not currentDbDataVal:
            # we'll be inserting a new value
            # print('DEBUG :: Tle() :: Inserting :: ' + str(dataVal) + ' :: ' + str(dataName))
            query = "INSERT INTO " \
                    "   tle.account_metadata " \
                    "SET " \
                    "   created = NOW(), " \
                    "   last_updated = NOW(), " \
                    "   data_value = %s, " \
                    "   data_name = %s"
        else:
            # we'll be updating the current value
            # print('DEBUG :: Tle() :: Updating :: ' + str(dataVal) + ' :: ' + str(dataName))
            query = "UPDATE " \
                    "   tle.account_metadata " \
                    "SET " \
                    "   last_updated = NOW(), " \
                    "   data_value = %s " \
                    "WHERE " \
                    "   data_name = %s"

        # run query
        try:
            cursor.execute(query, (str(dataVal), str(dataName)))
            dbConn.commit()
        except mysql.connector.Error as error:
            print('DEBUG :: Tle() :: setMetadata() :: MySQL Error :: ' + str(error.errno) + ' :: ' + error.msg)
            # insert failed
            return False

        # close db connection
        dbConn.close()

        return True

    def syncMetadata(self, dbConfData, syncDir):
        """
        Description:
            Syncs metadata to or from the database

        Params:
            syncDir [INT]: specifies which direction to sync - to (0) or from (1)

        Output:
            Bool
        """

        # verify syncDir var is valid
        if syncDir == 0:
            # sync TO the database
            if (
                not self.setMetadataInDb(dbConfData, 'balance', self.balance)
                or not self.setMetadataInDb(dbConfData, 'total_money_spent', self.moneySpent)
                or not self.setMetadataInDb(dbConfData, 'total_profit', self.profit)
                or not self.setMetadataInDb(dbConfData, 'trade_risk_lvl', self.tradeRiskLvl)
            ):
                return False
        elif syncDir == 1:
            # sync FROM the database
            # get balance
            self.balance = self.getMetadataFromDb(dbConfData, 'balance')
            # get total money spent
            self.moneySpent = self.getMetadataFromDb(dbConfData, 'total_money_spent')
            # get total profit
            self.profit = self.getMetadataFromDb(dbConfData, 'total_profit')
            # get trade risk level
            self.tradeRiskLvl = self.getMetadataFromDb(dbConfData, 'trade_risk_lvl')

            if (
                not self.balance
                or not self.moneySpent
                or not self.profit
                or not self.tradeRiskLvl
            ):
                raise RuntimeError('TLE :: syncMetadata() :: could not find sync data')
        else:
            # invalid sync direction
            raise ValueError('TLE :: syncMetadata() :: invalid sync direction specified')

        return True

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