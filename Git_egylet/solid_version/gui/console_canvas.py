import curses
import os
from typing import List

from bosch_ASDIIE.Git_egylet.solid_version.core.enum.map import Coordinates, MapSize
from bosch_ASDIIE.Git_egylet.solid_version.core.interfaces.canvas import Canvas
from bosch_ASDIIE.Git_egylet.solid_version.core.enum.screen import Screen


class ConsoleCanvas(Canvas):
    """
    This class makes a graphical user interface (GUI) for the game
    """
    def __init__(self, map_size: MapSize, curses_screen: Screen):
        self.width = map_size.col_num + 1
        self.height = map_size.col_num + 1
        self.crs_screen = curses_screen
        self.map = self._get_empty_map()

    def clear(self):
        """
        This function clears the map
        :return:
        """
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)
        self.map = self._get_empty_map()
        self.crs_screen.clear()

    def draw_dots(self, coordinates: List[Coordinates], object_type: str):
        """
        This function is responsible for the visualization of different types of objects
        :param coordinates: The coordinates of the current object
        :param object_type: The type of the object
        :return:
        """
        for dot in coordinates:
            if object_type == 'pacman':
                self.map[dot.row][dot.col] = "x"
            elif object_type == 'pellets':
                self.map[dot.row][dot.col] = "O"
            elif object_type == 'walls':
                self.map[dot.row][dot.col] = "|"

    def render(self):
        for num_row, row in enumerate(self.map):
            try:
                self.crs_screen.addstr(num_row, 0, "".join(row) + "\n")
            except curses.error:
                pass
        self.crs_screen.refresh()

    def _get_empty_map(self):
        screen = []
        for _ in range(self.height):
            screen.append([" "] * self.width)
        return screen

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width