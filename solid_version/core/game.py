import time

from bosch_ASDIIE.solid_version.core.key_listener import KeyboardListener
from bosch_ASDIIE.solid_version.core.snake_game_state import SnakeGameState
from bosch_ASDIIE.solid_version.core.visualizer import Visualizer


class Game:
    """
    Class for the game, managing it from start to end
    """
    GAME_SPEED = 0.4

    def __init__(self,
                 keyboard_listener: KeyboardListener,
                 game_state: SnakeGameState,
                 visualizer: Visualizer,
                 ):

        self.keyboard_listener = keyboard_listener
        self.game_state = game_state
        self.visualizer = visualizer

    def run(self):
        can_continue = True
        while can_continue:
            if self.keyboard_listener.has_happened():
                key_event = self.keyboard_listener.read_last_key_event()
                self.game_state.take_action(key_event)
            self.game_state.step()
            can_continue = not self.game_state.is_terminated()
            self.visualizer.render()
            time.sleep(self.GAME_SPEED)
