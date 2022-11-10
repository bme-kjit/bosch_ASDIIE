from collections import deque
from typing import Deque

from bosch_ASDIIE.Git_egylet.solid_version.core.canvas import Canvas
from bosch_ASDIIE.Git_egylet.solid_version.core.map import Coordinates, MapSize
from bosch_ASDIIE.Git_egylet.solid_version.core.game_element import GameElement
from bosch_ASDIIE.Git_egylet.solid_version.core.visualizable import Visualizable


class Wallgenerator(GameElement, Visualizable):
    """
    A visualizable class for generating walls and handling collision
    """
    def __init__(self,
                 body: Deque[Coordinates] = None,
                 map_size: MapSize = None):
        if body is None:
            self.body_parts = deque([
                Coordinates(2, 2), Coordinates(3, 3), Coordinates(4, 4)
            ])
        else:
            self.body_parts = body
        if map_size is None:
            map_size = MapSize(10, 10)

    def draw(self, canvas: Canvas):
        canvas.draw_walls(self.body_parts)