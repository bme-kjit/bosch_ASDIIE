"""
*********************************************************************
*********************************************************************
PROJECT_NAME : PacMan
FILENAME     : test_Movable.py
AUTHOR       : Bozsóki Márk
UNIVERSITY   : BME
TEAM         : SegmentFault
*********************************************************************
*********************************************************************
Short description
--------------------------------------------------------------------
source/dynamic_elements/movables/Movable.py testing module

To run this module:
python3 -m unittest test.source.dynamic_elements.movables.test_Movable

see README for help
********************************************************************
********************************************************************
"""

import unittest

from source.dynamic_elements.movables.Movable import Movable
from source.dynamic_elements.Direction import Direction

class test_Movable(unittest.TestCase):

    def test_next_position(self):
        """
        Testing next_position function in all possible directions
        """
        movable = Movable()
        current_position = (0,0)

        self.assertTupleEqual(movable.next_position(current_position, Direction.Right), (0,1))
        self.assertTupleEqual(movable.next_position(current_position, Direction.Down), (1,0))
        self.assertTupleEqual(movable.next_position(current_position, Direction.Left), (0,-1))
        self.assertTupleEqual(movable.next_position(current_position, Direction.Up), (-1,0))


    def test_last_position(self):
        """
        Testing last_position function in all possible directions
        """
        movable = Movable()
        current_position = (0,0)

        self.assertTupleEqual(movable.last_position(current_position, Direction.Right), (0,-1))
        self.assertTupleEqual(movable.last_position(current_position, Direction.Down), (-1,0))
        self.assertTupleEqual(movable.last_position(current_position, Direction.Left), (0,1))
        self.assertTupleEqual(movable.last_position(current_position, Direction.Up), (1,0))


if __name__ == "__main__":
    unittest.main()