from abc import ABC, abstractmethod

from core.interface.canvas import Canvas


class Visualizable(ABC):
    @abstractmethod
    def draw(self, canvas: Canvas) -> None:
        """
        Draw the objects on the canvas.
        :param canvas: the canvas where it draws.
        :return: None
        """
        pass
