from __future__ import annotations
import abc
from abc import ABC

from TeamSix.solid_version.enums.direction import Direction
from TeamSix.solid_version.interfaces.field import Field
from TeamSix.solid_version.interfaces.interactable import Interactable
from TeamSix.solid_version.display.drawingService import DrawingService
from TeamSix.solid_version.enums.direction import Direction


class Pacman(Interactable, ABC):
    """
    Pacman implementation
    """
    has_moved = False

    def __init__(self, field: Field, direction: Direction = Direction.RIGHT.value):
        super().__init__(field)
        self.direction = direction
        self.points = 0
        self.dead = False

    def collide_with(self, i: Interactable):
        """
        Iteraction with other interactables
        @param i: Interactable
        @return:
        """
        i.hit_by(self)

    def move(self, d: Direction):
        """
        Move to the next field in the direction
        @param d: Direction
        @return:
        """
        if self.field and not self.has_moved:
            neighbor = self.field.get_neighbor(d)
            if neighbor:
                self.field.remove(self)
                neighbor.accept(self)
            else:
                self.die()
            self.has_moved = True

    def add_points(self, p: int):
        """
        Add point
        @param p: points
        @return:
        """
        self.points = self.points + p

    def hit_by(self, i: Interactable):
        """
        Interaction when other interactables meets with pacman
        @param i: Interactable
        @return:
        """
        return

    def draw(self, service: DrawingService):
        """
        Display pacman
        @param service:
        @return:
        """
        service.draw_pacman(self.field.position_x, self.field.position_y)

    def die(self):
        """
        Kills pacman
        @return:
        """
        self.dead = True

    def step(self):
        """
        Advances one step
        @return:
        """
        self.move(self.direction)
