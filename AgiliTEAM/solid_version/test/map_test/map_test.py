import unittest
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath("../../core/game.py"))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from core.game_element.walls import Walls
from core.misc.map import Coordinates, MapSize


class MapTest(unittest.TestCase):

    def test_MapMaking_NotEmpty(self):
        map_size = MapSize(5, 5)
        internal_walls = [Coordinates(3, 3)]
        walls = Walls(map_size=map_size, internal_walls=internal_walls)
        self.assertTrue(walls.pos.count(Coordinates(3, 3)) == 1, "No inner wall detected on the pitch")

    def test_MapMaking_Borders(self):
        map_size = MapSize(3, 3)
        walls = Walls(map_size=map_size)

        for row in range(map_size.row_num):
            self.assertEqual(walls.pos.count(Coordinates(row, 0)), 1, "The pitch generation is wrong. There is a leak"
                                                                      "in the pitch borders")
            self.assertEqual(walls.pos.count(Coordinates(row, map_size.col_num - 1)), 1,
                             "The pitch generation is wrong. There is a leak in the pitch borders")

    def test_MapMaking_Empty(self):
        map_size = MapSize(5, 5)
        internal_walls = [Coordinates(3, 3)]
        walls = Walls(map_size=map_size, internal_walls=internal_walls)
        self.assertTrue(walls.pos.count(Coordinates(2, 2)) == 0, "Inner wall detected")
