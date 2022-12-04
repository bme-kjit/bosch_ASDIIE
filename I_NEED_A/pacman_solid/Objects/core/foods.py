from typing import Deque

from Objects.core.canvas import Canvas

from Objects.core.map import Coordinates, MapVariation
from Objects.core.visualizable import Visualizable


class Foods(Visualizable):
    """
      Class for foods.
    """

    def __init__(self, map_variation: MapVariation = None):
        self.map = map_variation

    def draw(self, canvas: Canvas):
        canvas.draw_foods(self.map.food_positions)