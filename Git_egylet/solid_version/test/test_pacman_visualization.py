from collections import deque
from typing import List

from bosch_ASDIIE.Git_egylet.solid_version.core.interfaces.canvas import Canvas
from bosch_ASDIIE.Git_egylet.solid_version.core.enum.key_event import KeyEvent
from bosch_ASDIIE.Git_egylet.solid_version.core.enum.map import Coordinates, MapSize
from bosch_ASDIIE.Git_egylet.solid_version.core.game_elements.pacman import Pacman
from bosch_ASDIIE.Git_egylet.solid_version.gui.console_canvas import ConsoleCanvas

class SpyCanvas(Canvas):
    def __init__(self, canvas: Canvas):
        self.canvas = canvas
        self._dots_on_canvas = []

    @property
    def dots_on_canvas(self):
        return self._dots_on_canvas

    def draw_dots(self, coordinates: List[Coordinates], object_type: str):
        self._dots_on_canvas.extend(coordinates)
        self.canvas.draw_dots(coordinates)

    def clear(self):
        self._dots_on_canvas = []

    def render(self):
        pass

def testCanvas_whenPacmanMoving_itAppearsOnNewCoordinates():
    canvas = ConsoleCanvas(10, 10)
    spy_canvas = SpyCanvas(canvas)
    pacman = Pacman(
        deque([Coordinates(0, 1), Coordinates(0, 2), Coordinates(0, 3)]),
        starting_direction=KeyEvent.RIGHT
    )
    pacman.draw(spy_canvas)
    dots_before_moving = spy_canvas.dots_on_canvas
    spy_canvas.clear()
    pacman.tick()
    pacman.draw(spy_canvas)
    dots_after_moving = spy_canvas.dots_on_canvas
    assert Coordinates(0, 1) in dots_before_moving and \
           Coordinates(0, 1) not in dots_after_moving, \
        "Pacman should not be displayed on the previous coordinates after moving."
    assert Coordinates(0, 4) in dots_before_moving and \
           Coordinates(0, 4) not in dots_after_moving, \
        "PacMan should be moved on canvas after moving."

def testCanvas_whenPacmanMoving_thenOppositeKeyEventDoesNotDoAnything():
    canvas = ConsoleCanvas(10, 10)
    spy_canvas = SpyCanvas(canvas)
    pacman = Pacman(
        deque([Coordinates(0, 1), Coordinates(0, 2), Coordinates(0, 3)]),
        starting_direction=KeyEvent.RIGHT
    )
    pacman.draw(spy_canvas)
    dots_before_moving = spy_canvas.dots_on_canvas
    spy_canvas.clear()
    pacman.take_action(KeyEvent.LEFT)
    pacman.tick()
    pacman.draw(spy_canvas)
    dots_after_moving = spy_canvas.dots_on_canvas
    assert Coordinates(0, 1) in dots_before_moving and \
           Coordinates(0, 1) not in dots_after_moving, \
        "Pacman should not be displayed on the previous coordinates after moving."
    assert Coordinates(0, 4) not in dots_before_moving and \
           Coordinates(0, 4) in dots_after_moving, \
        "Pacman should be moved towards the original direction " \
        "after pacman got opposite KeyEvent."
