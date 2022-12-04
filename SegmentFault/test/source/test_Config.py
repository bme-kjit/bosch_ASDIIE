"""
*********************************************************************
*********************************************************************
PROJECT_NAME : PacMan
FILENAME     : test_Config.py
AUTHOR       : 
UNIVERSITY   : BME
TEAM         : SegmentFault
*********************************************************************
*********************************************************************
Short description
--------------------------------------------------------------------
source/Config.py testing module

To run this module:
python3 -m unittest test.source.test_Config

see README for help
********************************************************************
********************************************************************
"""

import unittest

#from source.Config import Config
from bosch_ASDIIE.SegmentFault.source.Config import *

class test_Config(unittest.TestCase):

    def test_GetGamemode(self):
        """
        Returned type check for GetGamemode function
        """
        config = Config()

        self.assertEqual(config.GetGamemode(), "sandbox")

    def test_GetGamemodetype(self):
        """
        Returned type check for GetGamemode function
        """
        config = Config()

        Gamemode = config.GetGamemode()
        self.assertIs(type(Gamemode), str)

    def test_GetTimeout(self):
        """
        Returned type check for GetTimeout function
        """
        config = Config()

        TimeoutLimit = config.GetTimeout()
        self.assertIs(type(TimeoutLimit), int)

    def test_GetMapdata(self):
        """
        Checks the returned filename extension
        """ 
        config = Config()

        self.assertRegex(config.GetMapdata(), ".*\.mapdat$")

    def test_fortype_GetGameSpeed(self):
        """
        Returned type check for GetGameSpeed function
        """
        config = Config()

        Gamespeed = config.GetGamespeed()
        self.assertIs(type(Gamespeed), float)

    def test_GetGameSpeed(self):
        """
        Returned value check for GetGameSpeed function by default the rate must be 1
        """

        config = Config()

        Gamespeed = config.GetGamespeed()
        self.assertEqual(Gamespeed, 1.0)

if __name__ == "__main__":
    unittest.main()