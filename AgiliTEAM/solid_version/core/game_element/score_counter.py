from core.interface.game_element import GameElement
from core.key_interaction.key_event import KeyEvent
from core.game_element.pellets import Pellets
from core.game_element.pacman import Pacman


class ScoreCounter(GameElement):

    def __init__(self,
                 base_score: int,
                 difficulty: float,
                 pacman: Pacman,
                 pellets: Pellets,
                 ):
        """
        The constructor of the score counter class which is responsible for counting the score(eaten pellets number).
        :param base_score: sets the score number for a pellet.
        :param difficulty: the difficulty decides that how the score calculation will happen(more the difficult, less the score)
        :param pacman: constructed pacman object.
        :param pellets: pellets object.
        """
        self.score_pellet = base_score * difficulty
        self.pacman = pacman
        self.pellets = pellets

        self.score = 0

    def take_action(self, key_event: KeyEvent) -> None:
        pass

    def tick(self) -> bool:
        """
        Calculates the score if pacman eats a chocolate.
        :return: return True
        """
        for pos in range(len(self.pellets.pos)):
            if self.pacman.pos[0] == self.pellets.pos[pos]:
                self.score += self.score_pellet
                self.pellets.pos.pop(pos)
                break

        return True
