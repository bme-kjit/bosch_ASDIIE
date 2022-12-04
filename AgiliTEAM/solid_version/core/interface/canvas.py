from abc import ABC, abstractmethod
from typing import List

from core.misc.map import Coordinates


class Canvas(ABC):
    @abstractmethod
    def draw_dots(self, coordinates: List[Coordinates], obj_type) -> None:
        """
        Abstract method. In each descendant it will draw them on the canvas.
        :param coordinates: coordinates which is wanted to be drawn.
        :param obj_type: type of the object
        :return: None
        """
        pass

    @abstractmethod
    def render(self) -> None:
        """
        Abstract method, responsible for rendering the objects.
        :return: None
        """
        pass

    @abstractmethod
    def clear(self) -> None:
        """
         Abstract method. In each descendant it will clear the canvas
        :return: None
        """
        pass

    @abstractmethod
    def get_height(self) -> int:
        """

        :return: returns the height of the canvas
        """
        pass

    @abstractmethod
    def get_width(self) -> int:
        """

        :return: returns the width of the canvas
        """
        pass
