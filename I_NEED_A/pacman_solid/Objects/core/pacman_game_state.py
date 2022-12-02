from typing import List

from Objects.core.game_element import GameElement
from Objects.core.get_action import KeyEvent


class PacmanGameState:
    """
    A class for managing the game state, handling actions of the game elements
    """
    def __init__(self, game_elements: List[GameElement]):
        self.game_elements = game_elements
        self._can_game_continue = True
        self.life = 100

    def step(self):
        for game_element in self.game_elements:
            self._can_game_continue = self._can_game_continue and game_element.tick()
        
        self.life -= 1

    def is_terminated(self):
        return not self._can_game_continue

    def take_action(self, key_event: KeyEvent):
        for game_element in self.game_elements:
            game_element.take_action(key_event)