from __future__ import annotations
from TeamSix.solid_version.interfaces.drawable import Drawable
from TeamSix.solid_version.enums.direction import Direction
from TeamSix.solid_version.interfaces.steppable import Steppable
from TeamSix.solid_version.interfaces.interactable import Interactable
from TeamSix.solid_version.display.drawingService import DrawingService
import abc


class Field(Steppable, Drawable):
    """
    Field abstraction
    """
    things: list[Interactable]
    neighbors = {
        'DOWN': None,
        'UP': None,
        'RIGHT': None,
        'LEFT': None,
    }
    position_x = None
    position_y = None

    def __init__(self, x, y):
        self.position_x = x
        self.position_y = y
        self.things = []
        self.neighbors = {
            'DOWN': None,
            'UP': None,
            'RIGHT': None,
            'LEFT': None,
        }

    def step(self):
        """
        Step on this field
        @return: None
        """
        for t in self.things:
            t.step()

    @abc.abstractmethod
    def accept(self, i: Interactable):
        """
        Field accepts an interactable through this method
        @param i: Interactable instance to accept
        @return: None
        """
        pass

    @abc.abstractmethod
    def remove(self, i: Interactable):
        """
        Remove from field
        @param i: Interactable intasnce to remove
        @return: None
        """
        pass

    def get_neighbor(self, d: Direction) -> Field:
        """
        Get neighbor in the direction
        @param d: Direction
        @return: Neighbor
        """
        return self.neighbors[d]

    def set_neighbor(self, d: Direction, f: Field) -> Field:
        """
        Set neighbor in the direction
        @param d: Direction
        @param f: Neighbor Field
        """
        self.neighbors[d] = f

    @abc.abstractmethod
    def draw(self, service: DrawingService):
        """
        Draw this field
        @param service: DrawingService
        @return:
        """
        pass
