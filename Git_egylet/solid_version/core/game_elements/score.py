from bosch_ASDIIE.Git_egylet.solid_version.core.interfaces.game_element import GameElement
from bosch_ASDIIE.Git_egylet.solid_version.core.enum.key_event import KeyEvent
from bosch_ASDIIE.Git_egylet.solid_version.core.game_elements.pacman import Pacman
from bosch_ASDIIE.Git_egylet.solid_version.core.objects.pellets import Pellets


class Score(GameElement):
    """
    This class is responsible for counting the score during the game
    """
    def __init__(self,
                 score_per_pellet: int,
                 pacman: Pacman,
                 pellets: Pellets,
                 ):
        self.score_per_pellet = score_per_pellet
        self.pacman = pacman
        self.pellets = pellets
        self.score = 0

    def take_action(self, key_event: KeyEvent):
        pass

    def tick(self) -> bool:
        """
        This function updates the score every timestep. It gives a point if the PacMan interacts with a pellet,
        then removing that pellet from the map.
        :return: A bool value which determines if the game can continue
        """
        for i in range(len(self.pellets.positions)):
            if self.pacman.position[0] == self.pellets.positions[i]:
                self.score += self.score_per_pellet
                self.pellets.positions.pop(i)
                break

        return True

    def get_score(self):
        """
        This function is responsible for getting the score of the game
        :return: The score collected through the game
        """
        score = self.score
        return score