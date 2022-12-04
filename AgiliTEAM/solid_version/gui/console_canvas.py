import os
from typing import List

from core.misc.map import Coordinates, MapSize
from core.interface.canvas import Canvas
from core.display.screen import Screen
from core.display.object_markers import ObjectMarkers


class ConsoleCanvas(Canvas):

    def __init__(self,
                 map_size: MapSize,
                 curses_screen: Screen):
        """
        The canvas class for the console version
        :param map_size: the size of the pitch where the game is played
        :param curses_screen: input screen.
        """
        self.width = map_size.col_num + 1
        self.height = map_size.col_num + 1
        self.crs_screen = curses_screen
        self.map = self._get_empty_map()

    def clear(self) -> None:
        """
        Clears everything from the screen.
        :return: None
        """
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)
        self.map = self._get_empty_map()
        self.crs_screen.clear()

    def draw_dots(self, coordinates: List[Coordinates], obj_type: ObjectMarkers) -> None:
        """
        Draw the objects on the canvas.
        :param coordinates: the coordinates to be drawn
        :param obj_type: the type of the object mark.
        :return: None
        """
        for dot in coordinates:
            self.map[dot.row][dot.col] = obj_type.value

    def render(self) -> None:
        """
        Responsible for rendering the objects on the screen and refreshing it.
        :return: None
        """
        for num_row, row in enumerate(self.map):
            self.crs_screen.addstr(num_row, 0, "".join(row) + "\n")
        self.crs_screen.refresh()

    def _get_empty_map(self) -> list:
        """
        Returns an empty map.
        :return: Empty map.
        """
        screen = []
        for height_pos in range(self.height):
            screen.append([" "] * self.width)
        return screen

    def get_height(self) -> int:
        """
        :return: The height of a pitch
        """
        return self.height

    def get_width(self) -> int:
        """
        :return: The width of a pitch
        """
        return self.width
