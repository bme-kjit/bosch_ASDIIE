from __future__ import annotations
import abc

from TeamSix.solid_version.interfaces.steppable import Steppable
from TeamSix.solid_version.display.drawingService import DrawingService
from TeamSix.solid_version.interfaces.drawable import Drawable


class Interactable(Drawable, Steppable):

    def __init__(self, field):
        self.field = field

    @abc.abstractmethod
    def collide_with(self, t: Interactable):
        pass

    @abc.abstractmethod
    def hit_by(self, p: Interactable):
        pass

    @abc.abstractmethod
    def draw(self, service: DrawingService):
        pass
    def step(self):
        return
