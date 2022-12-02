import abc
from TeamSix.solid_version.display.drawingService import DrawingService


class Drawable(abc.ABC):
    draw_rank = 1
    
    @abc.abstractmethod
    def draw(self, service: DrawingService):
        pass
