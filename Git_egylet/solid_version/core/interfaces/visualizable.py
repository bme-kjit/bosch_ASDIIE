from abc import ABC, abstractmethod

from bosch_ASDIIE.Git_egylet.solid_version.core.interfaces.canvas import Canvas


class Visualizable(ABC):
    @abstractmethod
    def draw(self, canvas: Canvas):
        pass