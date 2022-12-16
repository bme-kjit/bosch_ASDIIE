from TeamSix.solid_version.display.drawingService import DrawingService
from TeamSix.solid_version.pacman.pacman import Pacman
from TeamSix.solid_version.interfaces.interactable import Interactable


class Coin(Interactable):
    """
    Coin implementation
    """
    POINT_VALUE = 1

    def __init__(self, field):
        super().__init__(field)

    def hit_by(self, p: Pacman):
        """
        Interaction when pacman eats this Coin
        @param p: Pacman
        @return: None
        """
        p.add_points(self.POINT_VALUE)
        self.field.remove(self)

    def collide_with(self, i: Interactable):
        """
        Interaction when encountering anything, blank since a Coin can't move
        @param i: Interactable
        @return:
        """
        return

    def draw(self, service: DrawingService):
        """
        Display on display
        @param service: DrawingService
        @return:
        """
        service.draw_coin(self.field.position_x, self.field.position_y)

    
