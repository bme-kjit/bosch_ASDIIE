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

from source.Config import Config

class test_Config(unittest.TestCase):

    def test_GetGamemode(self):
        """ Returned type check for GetGamemode function
        """
        config = Config()

        self.assertEqual(config.GetGamemode(), "sandbox")

    def test_GetTimeout(self):
        """ Returned type check for GetTimeout function
        """
        pass

    def test_GetMapdata(self):
        """
        """
        pass

    def test_GetGameSpeed(self):
        """ Returned type and value check for GetTimeout function
        """
        
        pass

if __name__ == "__main__":
    unittest.main()