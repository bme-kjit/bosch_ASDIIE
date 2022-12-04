from typing import List
import math
import random

from core.key_interaction.key_event import KeyEvent
from core.interface.game_element import GameElement
from core.interface.visualizable import Visualizable
from core.key_interaction.move import MovingTransformation
from core.interface.canvas import Canvas
from core.misc.map import MapSize, Coordinates
from core.misc.pos_generator import PositionGenerator
from core.display.object_markers import ObjectMarkers


class Ghosts(GameElement, Visualizable):

    GHOST_START_DIRECTION = KeyEvent.RIGHT

    def __init__(self,
                 map_size: MapSize = MapSize(10, 10),
                 num_ghosts: int = 4,
                 known_pos: List[List[Coordinates]] = None,
                 step_confidence: float = 0.8,
                 walls_pos: List[Coordinates] = None
                 ):
        """
        Constructor of the ghost class.
        :param map_size: the size of the pitch where the game is played
        :param num_ghosts: Number of the ghost in the game
        :param known_pos: List of the actually placed item's coordinates in the pitch
        :param step_confidence: number between 0 and 1. Sets how good the step should be
        """
        if known_pos is not None:
            self.known_pos = [item for sublist in known_pos for item in sublist]
        else:
            self.known_pos = []

        self.step_confidence = step_confidence
        self.event = self.GHOST_START_DIRECTION

        pos_generator = PositionGenerator(map_size, self.known_pos)
        self.pos, self.known_pos = pos_generator.generate_pos(num_of_pos=num_ghosts)

        self.walls_pos = walls_pos
        self.moving_transformation_ghost = MovingTransformation(self.event, map_size, self.walls_pos)

    def __take_best_action__(self, pacman_position: Coordinates, ghost_index: int) -> None:
        """
        It takes the best action to catch pacman
        :param pacman_position: position of the pacman
        :param ghost_index: index of the current ghost
        :return: None
        """
        current_ghost_pos = self.pos[ghost_index]
        ghost_pacman_angle = math.atan2((pacman_position.row - current_ghost_pos.row),
                                        (pacman_position.col - current_ghost_pos.col))
        direction_component_in_x = math.cos(ghost_pacman_angle)
        direction_component_in_y = math.sin(ghost_pacman_angle)
        is_it_vertical_step = True if abs(direction_component_in_x) < abs(direction_component_in_y) else False
        greater_direction_component = direction_component_in_y if abs(direction_component_in_x) < abs(
            direction_component_in_y) else direction_component_in_x

        if 0 > greater_direction_component and is_it_vertical_step:
            self.event = KeyEvent.UP
        elif 0 < greater_direction_component and is_it_vertical_step:
            self.event = KeyEvent.DOWN
        elif 0 > greater_direction_component and not is_it_vertical_step:
            self.event = KeyEvent.LEFT
        elif 0 < greater_direction_component and not is_it_vertical_step:
            self.event = KeyEvent.RIGHT

        self.moving_transformation_ghost.direction = self.event
        self.pos[ghost_index] = self.moving_transformation_ghost(self.pos[ghost_index])

    def __take_random_action__(self, ghost_index: int) -> None:
        """
        Takes a random action
        :param ghost_index: index of the ghost
        :return: None
        """
        self.event = random.randrange(1, 4)
        self.pos[ghost_index] = self.moving_transformation_ghost(self.pos[ghost_index])

    def take_action(self, pacman_position: Coordinates) -> None:
        """
        Take action of all ghosts.
        :param pacman_position: position of the pacman
        :return: None
        """
        for current_ghost_index in range(len(self.pos)):
            if random.uniform(0, 1) >= self.step_confidence:
                self.__take_best_action__(pacman_position, current_ghost_index)
            else:
                self.__take_random_action__(current_ghost_index)

    def tick(self, pacman_position: Coordinates) -> bool:
        """
        Performs the action in the current time step
        :param pacman_position: position of the pacman.
        :return:
        """
        self.take_action(pacman_position)

        return True

    def draw(self, canvas: Canvas) -> None:
        """
        Draws the ghosts on the canvas.
        :param canvas: canvas where we would like to draw.
        :return: None
        """
        canvas.draw_dots(self.pos, ObjectMarkers.GHOSTS)
