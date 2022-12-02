from bosch_ASDIIE.Git_egylet.solid_version.core.interfaces.game_element import GameElement
from bosch_ASDIIE.Git_egylet.solid_version.core.enum.key_event import KeyEvent
from bosch_ASDIIE.Git_egylet.solid_version.core.game_elements.pacman import Pacman
from bosch_ASDIIE.Git_egylet.solid_version.core.objects.walls import Walls


class Terminate(GameElement):
    """
    This class is responsible for terminating the game if the PacMan interacts with a wall
    """
    def __init__(self,
                 pacman: Pacman,
                 walls: Walls,
                 ):
        self.pacman = pacman
        self.walls = walls

    def take_action(self, key_event: KeyEvent):
        pass

    def tick(self) -> bool:
        """
        This function terminates the game if the PacMan interacts with a wall
        :return: A bool value which determines if the game can continue
        """
        for i in range(len(self.walls.positions)):
            if self.pacman.position[0] == self.walls.positions[i]:
                return False

        return True