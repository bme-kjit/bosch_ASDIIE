from TeamSix.solid_version.display.drawingService import DrawingService
from TeamSix.solid_version.interfaces.field import Field
from TeamSix.solid_version.pacman.pacman import Pacman
from TeamSix.solid_version.interfaces.interactable import Interactable


class Wall(Field):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.things = []

    def accept(self, i: Interactable):
        if type(i) is Pacman:
            i.die()
        self.things.append(i)
        i.field = self

    def remove(self, i: Interactable):
        self.things.remove(i)

    def draw(self, service: DrawingService):
        service.draw_field(self.position_x, self.position_y, 'WALL')
