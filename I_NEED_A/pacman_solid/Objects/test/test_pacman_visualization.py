from collections import deque
from typing import List

from Objects.core.canvas import Canvas
from Objects.core.get_action import KeyEvent
from Objects.core.map import Coordinates, MapVariation
from Objects.core.pacman import Pacman
from Objects.gui.console_canvas import ConsoleCanvas
from Objects.core.screen import Screen


class SpyCanvas(Canvas):
    def __init__(self, canvas: Canvas):
        self.canvas = canvas
        self._pacman_position = None
        self._pacman_score = None

    @property
    def pacman_position(self):
        return self._pacman_position

    @property
    def pacman_score(self):
        return self._pacman_score

    def draw_pacman(self, coordinates: List[Coordinates]):
        self._pacman_position = coordinates

    def draw_foods(self, coordinates: List[Coordinates]):
        pass

    def draw_walls(self, coordinates: List[Coordinates]):
        pass

    def draw_foods(self, coordinates: List[Coordinates]):
        pass

    def draw_info(self, life: int):
        self._pacman_score = life


    def clear(self):
        self._dots_on_canvas = []

    def render(self):
        pass

def testCanvas_whenPacmanHitTheEndOfCanvas_DoesNotDoAnything():
    """
    If Pacman reaches the wall (every side of map)  , can1t go forward
    """
    map = MapVariation()
    screen = Screen()
    canvas = ConsoleCanvas(map, screen)
    spy_canvas = SpyCanvas(canvas)
    pacman = Pacman(
        None,
        starting_direction=KeyEvent.LEFT,
        map_variation=map
    )
    pacman.tick()
    pacman.tick()
    pacman.take_action(KeyEvent.UP)
    pacman.tick()
    pacman.tick()
    pacman.take_action(KeyEvent.LEFT)
    pacman.tick()
    pacman.tick()
    pacman.draw(spy_canvas)
    body_on_canvas = spy_canvas.pacman_position
    assert Coordinates(1, 1).col == body_on_canvas.col
    assert Coordinates(1, 1).row == body_on_canvas.row


def testCanvas_whenPacman_step_the_scoreIsLowered():
    """
    If Pacman reaches the wall (every side of map)  , can1t go forward
    """
    map = MapVariation()
    screen = Screen()
    canvas = ConsoleCanvas(map, screen)
    spy_canvas = SpyCanvas(canvas)
    pacman = Pacman(
        None,
        starting_direction=KeyEvent.LEFT,
        map_variation=map
    )

    pacman.tick()
    pacman.draw(spy_canvas)
    init_score = spy_canvas.pacman_score

    pacman.tick()
    pacman.draw(spy_canvas)
    assert init_score > spy_canvas.pacman_score

    pacman.tick()
    pacman.draw(spy_canvas)
    assert init_score > spy_canvas.pacman_score

    pacman.tick()
    pacman.draw(spy_canvas)
    assert init_score > spy_canvas.pacman_score





