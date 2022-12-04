import time

from core.key_interaction.key_listener import KeyListener
from core.pacman_game_state import PacmanGameState
from core.display.visualizer import Visualizer


class Game:

    def __init__(self,
                 keyboard_listener: KeyListener,
                 game_state: PacmanGameState,
                 visualizer: Visualizer,
                 game_speed: float,
                 ):
        """
        Class for the game, managing it from start to end
        :param keyboard_listener: Keyboard listener object for keyboard scanning.
        :param game_state: PacmanGameState object for game elements
        :param visualizer: Visualizer object for rendering game elements.
        :param game_speed: speed of the game.
        """
        self.keyboard_listener = keyboard_listener
        self.game_state = game_state
        self.visualizer = visualizer
        self.game_speed = game_speed

    def run(self) -> None:
        """
        Runs the game loop.
        :return: None
        """
        can_continue = True

        while can_continue:
            if self.keyboard_listener.has_happened():
                key_event = self.keyboard_listener.read_last_key_event()
                self.game_state.take_action(key_event)
            self.game_state.step()
            can_continue = not self.game_state.is_terminated()
            self.visualizer.render()
            time.sleep(self.game_speed)
