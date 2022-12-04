from typing import List, Tuple
import numpy as np

from core.misc.map import MapSize, Coordinates


class PositionGenerator:

    def __init__(self,
                 map_size: MapSize,
                 known_pos: List[Coordinates]):
        """
        Constructor of the PositionGenerator
        :param map_size: the size of the pitch where the game is played
        :param known_pos: list of the actually placed item's coordinates in the pitch
        """
        self.map_size = map_size
        self.known_pos = known_pos

    def generate_pos(self, num_of_pos: int) -> Tuple[List[Coordinates], List[Coordinates]]:
        """
        Generate positions of an object.
        :param num_of_pos: The number of the generated positions.
        :return: Return a tuple of coordinates of the generated positions.
        """
        pos_list = []
        for pos_num in range(num_of_pos):
            pos = Coordinates(np.random.randint(self.map_size[0]), np.random.randint(self.map_size[1]))
            while pos in self.known_pos:
                pos = Coordinates(np.random.randint(self.map_size[0]), np.random.randint(self.map_size[1]))
            pos_list.append(pos)
            self.known_pos.append(pos)

        return pos_list, self.known_pos
