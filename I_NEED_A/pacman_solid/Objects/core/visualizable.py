
from abc import ABC, abstractmethod

from Objects.core.canvas import Canvas


class Visualizable(ABC):
    @abstractmethod
    def draw(self, canvas: Canvas):
        pass