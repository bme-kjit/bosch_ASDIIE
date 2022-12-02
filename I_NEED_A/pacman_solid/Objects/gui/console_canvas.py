import os
from typing import List

from Objects.core.map import Coordinates, MapVariation
from Objects.core.canvas import Canvas
from Objects.core.screen import Screen


class ConsoleCanvas(Canvas):
    """
    The canvas class for the console version
    """

    def __init__(self,
                 map_variation: MapVariation,
                 curses_screen: Screen):

        self.crs_screen = curses_screen
        self.map_variation = map_variation
        self.raw_map = map_variation.get_map()
        self.map = self._get_empty_map()

    def clear(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)
        self.map = self._get_empty_map()
        self.crs_screen.clear()

    def draw_pacman(self, coordinates: List[Coordinates]):
        self.map[coordinates.row][coordinates.col] = \
            self.map_variation.get_annotation("pacman")
    
    def draw_walls(self, coordinates: List[Coordinates]):
        for coordinate in coordinates:
            self.map[coordinate.row][coordinate.col] = \
            self.map_variation.get_annotation("wall")
    
    def draw_foods(self, coordinates: List[Coordinates]):
        for coordinate in coordinates:
            self.map[coordinate.row][coordinate.col] = \
            self.map_variation.get_annotation("food")
    
    def draw_info(self, life: int):
        self.map[-1] = [char for char in f"score: {life}"]

    def render(self):
        for num_row, row in enumerate(self.map):
            try:
                self.crs_screen.addstr(num_row, 0, "".join(row) + "\n")
            except:
                raise "The terminal screen is too small for visualization."
        self.crs_screen.refresh()

    def _get_empty_map(self):
        screen = []
        for line in self.raw_map:
            line = [char if (char == self.map_variation.get_annotation("wall") or
                char == " ") else " " for char in line]
            screen.append(line)
        screen.append([]) # for life
        return screen