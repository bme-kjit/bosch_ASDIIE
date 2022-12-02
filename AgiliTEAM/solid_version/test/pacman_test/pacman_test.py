import unittest
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath("../../core/game.py"))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from core.key_interaction.key_event import KeyEvent
from core.pacman_game_state import PacmanGameState
from core.game_element.pacman import Pacman
from core.misc.map import Coordinates, MapSize


class GameStateTest(unittest.TestCase):
    def test_WhenOneStep_IsTerminatedFalse(self):
        pacman_game_state = PacmanGameState([])
        pacman_game_state.step()
        self.assertFalse(pacman_game_state.is_terminated(),
                         "The initialized game should not step into terminated state.")

    def test_PacmanStepFunction(self):
        pacman = Pacman(body=[Coordinates(5, 5)], map_size=MapSize(10, 10))
        test_game_state = PacmanGameState([pacman])
        test_game_state.take_action(KeyEvent.UP)
        test_game_state.step()
        self.assertTrue(pacman.get_pacman_position() == Coordinates(4, 5), "Error during step, value mismatch")

    def test_PacmanCanNotLeaveThePitch_TopLeftCornerPos(self):
        pacman = Pacman(body=[Coordinates(1, 1)], map_size=MapSize(3, 3))
        test_game_state = PacmanGameState([pacman])
        test_game_state.take_action(KeyEvent.UP)
        test_game_state.step()
        test_game_state.take_action(KeyEvent.LEFT)
        test_game_state.step()
        self.assertTrue(pacman.get_pacman_position() == Coordinates(0, 0), "Error during step, value mismatch")

    def test_PacmanWithWalls(self):
        map_size = MapSize(2, 2)
        pacman = Pacman(body=[Coordinates(1, 1)], map_size=map_size)
        walls = Walls(map_size=map_size)
        test_game_state = PacmanGameState([pacman, walls])
        test_game_state.take_action(KeyEvent.UP)
        test_game_state.step()
        self.assertTrue(test_game_state.is_terminated(), "The game should have ended")
