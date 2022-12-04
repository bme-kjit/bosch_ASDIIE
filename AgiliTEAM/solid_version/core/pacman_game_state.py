from typing import List

from core.interface.game_element import GameElement
from core.key_interaction.key_event import KeyEvent
from core.game_element.ghosts import Ghosts
from core.game_element.pacman import Pacman
from core.game_element.walls import Walls


class PacmanGameState:

    def __init__(self, game_elements: List[GameElement]):
        """
        Constructor of the game elements. Creates a configuration for a game given the elements.
        :param game_elements: list of the given game elements.
        """
        self.game_elements = game_elements
        self._can_game_continue = True

    def step(self) -> None:
        """
        Execute every step function for every game element object.
        :return: None
        """
        current_pacman_pos = None
        for game_element in self.game_elements:
            if isinstance(game_element, Pacman):
                self._can_game_continue = self._can_game_continue and game_element.tick()
                current_pacman_pos = game_element.get_pacman_position()
                continue
            elif isinstance(game_element, Ghosts):
                self._can_game_continue = self._can_game_continue and game_element.tick(current_pacman_pos)
                continue
            elif isinstance(game_element, Walls):
                self._can_game_continue = self._can_game_continue and game_element.tick(current_pacman_pos)
                continue
            else:
                self._can_game_continue = self._can_game_continue and game_element.tick()

    def is_terminated(self) -> bool:
        """
        Checks that the game is terminated or not.
        :return: True if it is. Otherwise False.
        """
        return not self._can_game_continue

    def take_action(self, key_event: KeyEvent) -> None:
        """
        Take action in every element.
        :param key_event: Keyboard event for action taking.
        :return: None
        """
        for game_element in self.game_elements:
            if isinstance(game_element, Ghosts):
                continue
            game_element.take_action(key_event)
