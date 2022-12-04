from typing import List

from core.key_interaction.key_event import KeyEvent
from core.interface.game_element import GameElement
from core.interface.visualizable import Visualizable
from core.interface.canvas import Canvas
from core.misc.map import MapSize, Coordinates
from core.misc.pos_generator import PositionGenerator
from core.display.object_markers import ObjectMarkers


class Pellets(GameElement, Visualizable):

    def __init__(self,
                 map_size: MapSize = MapSize(10, 10),
                 num_pellets: int = 10,
                 known_pos: List[List[Coordinates]] = None,
                 ):
        """
        Constructor of the pellets.
        :param map_size: the size of the pitch where the game is played
        :param num_pellets: the number of the pellets in the game
        :param known_pos: list of the actually placed item's coordinates in the pitch
        """
        if known_pos is not None:
            self.known_pos = [item for sublist in known_pos for item in sublist]
        else:
            self.known_pos = []

        pos_generator = PositionGenerator(map_size, self.known_pos)

        self.pos, self.known_pos = pos_generator.generate_pos(num_of_pos=num_pellets)

    def take_action(self, key_event: KeyEvent) -> None:
        """

        """
        pass

    @staticmethod
    def tick() -> bool:
        """

        """
        return True

    def draw(self, canvas: Canvas) -> None:
        """
        Draws all the pellets on the canvas.
        :param canvas:
        :return: None
        """
        canvas.draw_dots(coordinates=self.pos, obj_type=ObjectMarkers.PELLETS)
