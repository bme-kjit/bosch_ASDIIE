from typing import List

from core.interface.canvas import Canvas
from core.interface.game_element import GameElement
from core.interface.visualizable import Visualizable
from core.key_interaction.key_event import KeyEvent
from core.misc.map import MapSize, Coordinates
from core.display.object_markers import ObjectMarkers


class Walls(GameElement, Visualizable):

    def __init__(self,
                 map_size: MapSize = MapSize(10, 10),
                 internal_walls: List[Coordinates] = None,
                 known_pos: List[List[Coordinates]] = None,
                 ):
        """
        Constructor of the walls
        :param map_size: the size of the pitch where the game is played
        :param internal_walls: the list of the walls inside the pitch
        :param known_pos: list of the actually placed item's coordinates in the pitch
        """
        if known_pos is not None:
            self.known_pos = [item for sublist in known_pos for item in sublist]
        else:
            self.known_pos = []

        self.pos = self.generate_pos(map_size=map_size)

        if internal_walls is not None:
            self.pos = self.append_internal_pos(internal_walls)

    def take_action(self, key_event: KeyEvent) -> None:
        """

        """
        pass

    def tick(self, pacman_position: Coordinates) -> bool:
        """
        Performs the check for pacman touching the wall
        :return: True if the pacman hit the wall, otherwise False
        """
        if pacman_position in self.pos:
            return False

        return True

    def draw(self, canvas: Canvas) -> None:
        """
        Draws the wall on the canvas
        :param canvas:
        :return: None
        """
        canvas.draw_dots(self.pos, ObjectMarkers.WALLS)

    @staticmethod
    def generate_pos(map_size: MapSize) -> List[Coordinates]:
        """
        Generate the positions of the borders in a given map
        :param map_size: size of the map
        :return: returns the coordinates of the borders
        """
        pos_list = []
        for num_row in range(map_size.row_num):
            pos_list.append(Coordinates(num_row, 0))
            pos_list.append(Coordinates(num_row, map_size.col_num - 1))

        for num_col in range(1, map_size.col_num - 1):
            pos_list.append(Coordinates(0, num_col))
            pos_list.append(Coordinates(map_size.row_num - 1, num_col))

        return pos_list

    def append_internal_pos(self, pos: List[Coordinates]) -> List[Coordinates]:
        """
        Append additional wall inside the pitch
        :param map_size: size of the map
        :return: returns the coordinates of the borders
        """
        pos_list = self.pos

        for coordinate in pos:
            if coordinate not in self.known_pos:
                pos_list.append(coordinate)

        return pos_list
