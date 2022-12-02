from __future__ import annotations
import abc
from abc import ABC

from TeamSix.solid_version.enums.direction import Direction
from TeamSix.solid_version.interfaces.field import Field
from TeamSix.solid_version.interfaces.interactable import Interactable
from TeamSix.solid_version.display.drawingService import DrawingService
from TeamSix.solid_version.enums.direction import Direction


class Pacman(Interactable, ABC):
    has_moved = False

    def __init__(self, field: Field, direction: Direction = Direction.RIGHT.value):
        super().__init__(field)
        self.direction = direction
        self.points = 0
        self.dead = False

    def collide_with(self, i: Interactable):
        i.hit_by(self)

    def move(self, d: Direction):
        if self.field and not self.has_moved:
            neighbor = self.field.get_neighbor(d)
            if neighbor:
                self.field.remove(self)
                neighbor.accept(self)
            else:
                self.die()
            self.has_moved = True

    def add_points(self, p):
        self.points = self.points + p

    def hit_by(self, i: Interactable):
        return

    def draw(self, service: DrawingService):
        service.draw_pacman(self.field.position_x, self.field.position_y)

    def die(self):
        self.dead = True

    def step(self):
        self.move(self.direction)
