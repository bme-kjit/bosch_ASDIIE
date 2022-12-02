import os

import numpy as np


class Visualizer:
    @staticmethod
    def _clear_console():
        """
        Clearing the console
        :return:
        """
        # Note: Cannot clear the console in PyCharm, only in terminal
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def _show_map(observation: np.ndarray):
        """
        Visualizing the current state of the game to the player
        :param observation: Array containing the map (np.ndarray)
        :return:
        """
        for line in observation:
            print(*line, sep='  ')

    @staticmethod
    def _show_score(curr_score: int):
        """
        Informing the user about the current score
        :param curr_score: Current score of the player (int)
        :return: -
        """
        print("\nCurrent score: ", curr_score)

    @staticmethod
    def _game_over(done: bool):
        """
        Informing the user that the game is over
        :param done: Game over flag
        :return: -
        """
        if done:
            print("\nGAME OVER")

    def render(self, observation: np.ndarray, curr_score: int, done: bool):
        """
        Renders the required information.
        :param observation: Array containing the map (np.ndarray)
        :param curr_score: Current score of the player (int)
        :param done: Game over flag (bool)
        :return:
        """
        self._clear_console()
        self._show_map(observation)
        self._show_score(curr_score)
        self._game_over(done)
