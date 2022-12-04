from typing import List

from core.interface.game_element import GameElement
from core.key_interaction.key_event import KeyEvent
from core.key_interaction.move import MovingTransformation
from core.interface.visualizable import Visualizable
from core.interface.canvas import Canvas
from core.misc.map import MapSize, Coordinates
from core.misc.pos_generator import PositionGenerator
from core.display.object_markers import ObjectMarkers


class Pacman(GameElement, Visualizable):

    def __init__(self,
                 body: List[Coordinates] = None,
                 starting_direction: KeyEvent = KeyEvent.RIGHT,
                 map_size: MapSize = MapSize(10, 10),
                 known_pos: List[List[Coordinates]] = None,
                 ):
        """
        Constructor of the pacman class.
        :param body: body position of the pacman
        :param starting_direction: the direction where the pacman starts to move in the 0th timestep
        :param map_size: the size of the pitch where the game is played
        :param known_pos: list of the actually placed item's coordinates in the pitch
        """
        if known_pos is not None:
            self.known_pos = [item for sublist in known_pos for item in sublist]
        else:
            self.known_pos = []

        if body is None:
            pos_generator = PositionGenerator(map_size, self.known_pos)
            self.pos, self.known_pos = pos_generator.generate_pos(1)
        else:
            self.pos = body

        self.moving_transformation = MovingTransformation(starting_direction, map_size)

    def take_action(self, key_event: KeyEvent) -> None:
        """
        Take action of the pacman given the key_event from the user.
        :param key_event: key_event from the user.
        :return: None
        """
        self.moving_transformation.direction = key_event

    def get_pacman_position(self) -> Coordinates:
        """
        Returns the position of the pacman
        :return:
        """
        return self.pos[0]

    def tick(self) -> bool:
        """
        Performs the moving transformation in the current time step
        :return: returns True
        """
        self.pos = [self.moving_transformation(self.pos[0])]
        return True

    def draw(self, canvas: Canvas) -> None:
        """
        Draws the pacman on the canvas.
        :param canvas:
        :return: None
        """
        canvas.draw_dots(self.pos, ObjectMarkers.PACMAN)
