from typing import Deque

from Objects.core.canvas import Canvas
from Objects.core.game_element import GameElement
from Objects.core.get_action import KeyEvent
from Objects.core.map import Coordinates, MapVariation
from Objects.core.visualizable import Visualizable


class MovingTransformation:
    """
       A class for handling keyboard events during playing
       """

    def __init__(self, direction: KeyEvent, map_variation: MapVariation):
        self.direction = direction
        self.map_variation = map_variation

    def __call__(self, coordinates: Coordinates) -> Coordinates:
        if self.direction == KeyEvent.UP:
            new_row = (coordinates.row - 1)
            return Coordinates(new_row, coordinates.col)
        elif self.direction == KeyEvent.LEFT:
            new_col = (coordinates.col - 1)
            return Coordinates(coordinates.row, new_col)
        elif self.direction == KeyEvent.DOWN:
            new_row = (coordinates.row + 1)
            return Coordinates(new_row, coordinates.col)
        elif self.direction == KeyEvent.RIGHT:
            new_col = (coordinates.col + 1)
            return Coordinates(coordinates.row, new_col)
        else:
            raise ValueError(f"There is no moving forward {self.direction} direction.")


    def _wall_limit(self, coordinates: Coordinates) -> bool:
        """
        Limit pac-man to step outside the map.
        :param coordinates(Coordinates): pacman's desired position to step
        :return (Coordinates): allowed position
        """
        desired_coordinates = (coordinates.row, coordinates.col)
        return desired_coordinates in self.map_variation.wall_positions



class Pacman(GameElement, Visualizable):
    """
      A game element and visualizable class, for handling pacman movement mainly,
      but visualizing is also represented here
    """
    def __init__(self,
                 body: Coordinates = None,
                 starting_direction: KeyEvent = KeyEvent.RIGHT,
                 map_variation: MapVariation = None):

        
        if body is None:
            self.body = map_variation.pacman_start_position
        else:
            if body in map_variation.wall_positions:
                raise f"The {body} starting position is on wall, choose other position."
            else:
                self.body = body
        
        self.map_variation = map_variation

        self.moving_transformation = MovingTransformation(starting_direction, map_variation)
        self.life_counter = 100



    def take_action(self, key_event: KeyEvent):
        self.moving_transformation.direction = key_event

    def tick(self):
        
        # navigate between walls
        desired_action = self.moving_transformation(self.body)
        if not self.moving_transformation._wall_limit(desired_action):
            self.body = desired_action
        
        # eat food
        if self.body in self.map_variation.food_positions:
            self.map_variation._remove_element_from_map(self.body)
            self.life_counter += 10
        
        # life counter
        self.life_counter = self.life_counter -1
        if self.life_counter != 0:
            return True
        else:
            print("Game over")
            return False


    def draw(self, canvas: Canvas):
        canvas.draw_pacman(self.body)
        canvas.draw_info(self.life_counter)