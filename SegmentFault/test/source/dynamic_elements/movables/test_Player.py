"""
*********************************************************************
*********************************************************************
PROJECT_NAME : PacMan
FILENAME     : test_Player.py
AUTHOR       : Bozsóki Márk
UNIVERSITY   : BME
TEAM         : SegmentFault
*********************************************************************
*********************************************************************
Short description
--------------------------------------------------------------------
source/dynamic_elements/movables/Player.py testing module

To run this module:
python3 -m unittest test.source.dynamic_elements.movables.test_Player

see README for help
********************************************************************
********************************************************************
"""

import unittest

from source.dynamic_elements.movables.Player import Player
from source.map.MapData import MapData
from source.dynamic_elements.Direction import Direction

class test_Player(unittest.TestCase):

    def test_set_score(self):
        """
        Testing the correct resived score on different collectables
        """
        mapdata = MapData()
        mapdata.collectables.points = [(1,1)]
        mapdata.collectables.coins = [(2,2)]

        player = Player(mapdata, (0,0), Direction.Down)
        
        # no collectable on the players position
        self.assertEqual(player.set_score(), 0)
        # point
        player.position = (1,1)
        self.assertEqual(player.set_score(), 10)

        # coin
        player.position = (2,2)
        self.assertEqual(player.set_score(), 20)

        #TODO: cherry and ghost implementation



if __name__ == "__main__":
    unittest.main()