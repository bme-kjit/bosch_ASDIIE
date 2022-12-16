import abc
from TeamSix.solid_version.display.drawingService import DrawingService


class Drawable(abc.ABC):
    """
    Drwawble interface
    """
    draw_rank = 1
    
    @abc.abstractmethod
    def draw(self, service: DrawingService):
        """
        Draw a game element using the service
        @param service: service implementation
        @return: None
        """
        pass
