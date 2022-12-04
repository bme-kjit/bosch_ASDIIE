from core.interface.game_element import GameElement
from core.key_interaction.key_event import KeyEvent
from core.game_element.ghosts import Ghosts
from core.game_element.pacman import Pacman


class DefeatChecker(GameElement):

    def __init__(self,
                 pacman: Pacman,
                 ghosts: Ghosts,
                 ):
        """
        Constructs the DefeatChecker class which is responsible for checking whether the ghosts managed to catch the pacman
        :param pacman: Pacman class which holds the components of the pacman
        :param ghosts: Ghosts class which holds the components of the ghosts
        """
        self.pacman = pacman
        self.ghosts = ghosts

    def take_action(self, key_event: KeyEvent) -> None:
        """
        """
        pass

    def tick(self) -> bool:
        """
        It checks whether the ghosts managed to catch the pacman.
        :return: Returns True in case of the ghosts managed to catch the pacman otherwise return False
        """
        for pos_actual_ghost in range(len(self.ghosts.pos)):
            if self.pacman.pos[0] == self.ghosts.pos[pos_actual_ghost]:
                return False

        return True
