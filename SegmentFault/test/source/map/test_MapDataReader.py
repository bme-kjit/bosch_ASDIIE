"""
*********************************************************************
*********************************************************************
PROJECT_NAME : PacMan
FILENAME     : test_MapdataReader.py
AUTHOR       : 
UNIVERSITY   : BME
TEAM         : SegmentFault
*********************************************************************
*********************************************************************
Short description
--------------------------------------------------------------------
source/map/MapDataReader.py testing module

To run this module:
python3 -m unittest test.source.map.test_MapDataReader

see README for help
********************************************************************
********************************************************************
"""

import unittest

from source.map.MapDataReader import MapDataReader

class test_MapDataReader(unittest.TestCase):

    def test_list_mapdatas(self):
        """ Testing that the list_mapdatas function returns the expected format
        """
        # itt regex legyen használva: elvárt formátum [MapName.mapdat]
        pass


if __name__ == "__main__":
    unittest.main()