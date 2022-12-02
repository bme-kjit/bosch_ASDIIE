from typing import List

from bosch_ASDIIE.Git_egylet.solid_version.core.interfaces.game_element import GameElement
from bosch_ASDIIE.Git_egylet.solid_version.core.enum.key_event import KeyEvent


class PacmanGameState:
    """
    This class is responsible for determining the current state of the game and handling the actions
    """
    def __init__(self, game_elements: List[GameElement]):
        self.game_elements = game_elements
        self._can_game_continue = True

    def step(self):
        for game_element in self.game_elements:
            self._can_game_continue = self._can_game_continue and game_element.tick()

    def is_terminated(self):
        return not self._can_game_continue

    def take_action(self, key_event: KeyEvent):
        for game_element in self.game_elements:
            game_element.take_action(key_event)