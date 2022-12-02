import numpy as np
from typing import List
from bosch_ASDIIE.Git_egylet.solid_version.core.enum.map import Coordinates, MapSize


class Objects:
    """
    This class is responsible for creating objects around the map
    """
    def make_objects(self, number: int, map_size: MapSize) -> List[Coordinates]:
        """
        This function creates objects across the map
        :param number: The number of objects to make
        :param map_size: The size of the map
        :return: A list of the coordinates of the created objects
        """
        positions = []
        for _ in range(number):
            position = Coordinates(np.random.randint(map_size[0]), np.random.randint(map_size[1]))
            positions.append(position)
        return positions