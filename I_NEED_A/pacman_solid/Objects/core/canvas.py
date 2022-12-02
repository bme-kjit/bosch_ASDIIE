from abc import ABC, abstractmethod
from typing import List

from Objects.core.map import Coordinates

class Canvas(ABC):
    @abstractmethod
    def draw_pacman(self, coordinates: Coordinates):
        pass
    
    @abstractmethod
    def draw_walls(self, coordinates: List[Coordinates]):
        pass

    @abstractmethod
    def draw_foods(self, coordinates: List[Coordinates]):
        pass

    @abstractmethod
    def draw_info(self, life: int):
        pass

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def clear(self):
        pass