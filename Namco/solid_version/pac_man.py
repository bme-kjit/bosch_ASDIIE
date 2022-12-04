import numpy as np
from bosch_ASDIIE_Namco.Namco.solid_version.constants import ActionEnum


class PacMan:
    def __init__(self, action_enum=ActionEnum, pos_x: int = 0, pos_y: int = 0):
        """
        Implements PacMan
        :param action_enum: constants for action selection (enum)
        :param pos_x: row that PacMan starts the game at
        :param pos_y: col that PacMan starts the game at
        """
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.UP = action_enum.UP.value
        self.LEFT = action_enum.LEFT.value
        self.DOWN = action_enum.DOWN.value
        self.RIGHT = action_enum.RIGHT.value

    def process_action(self, action: str):
        """
        Moves PacMan in the desired direction
        :param action: current user input (w, a, s or d) (str)
        :return: Current x and y coordinate of PacMan [int, int]
        """
        # Moving up
        if action == self.UP:
            self.pos_x -= 1
        # Moving left
        elif action == self.LEFT:
            self.pos_y -= 1
        # Moving down
        elif action == self.DOWN:
            self.pos_x += 1
        # Moving right
        elif action == self.RIGHT:
            self.pos_y += 1

    def generate_init_pos(self, _map: np.ndarray, map_size: int, restricted_slot):
        """
        Determining the agent's initial position to a non-restricted area
        :return: -
        """
        while _map[self.pos_x][self.pos_y] == restricted_slot:
            self.pos_x = np.random.randint(map_size)
            self.pos_y = np.random.randint(map_size)

    @property
    def position(self):
        """
        Returns PacMan's current x and y coordinate
        :return: x and y coordinate of PacMan
        """
        return self.pos_x, self.pos_y
