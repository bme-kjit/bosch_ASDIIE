from __future__ import annotations
import abc

from TeamSix.solid_version.interfaces.steppable import Steppable
from TeamSix.solid_version.display.drawingService import DrawingService
from TeamSix.solid_version.interfaces.drawable import Drawable


class Interactable(Drawable, Steppable):
    """
    Interactable interface
    """
    def __init__(self, field):
        self.field = field

    @abc.abstractmethod
    def collide_with(self, t: Interactable):
        """
        Handle interaction with other interactables
        @param t: Other interactable
        @return:
        """
        pass

    @abc.abstractmethod
    def hit_by(self, p: Interactable):
        """
        Handle interaction when other interactables meet this instance
        @param p:
        @return:
        """
        pass

    @abc.abstractmethod
    def draw(self, service: DrawingService):
        """
        Draw this element on the screen
        @param service: DrawingServcie implementation
        @return:
        """
        pass
    def step(self):
        """
        Advance one step
        @return:
        """
        return
