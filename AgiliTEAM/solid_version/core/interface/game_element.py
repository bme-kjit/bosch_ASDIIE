from abc import ABC, abstractmethod

from core.key_interaction.key_event import KeyEvent


class GameElement(ABC):
    @abstractmethod
    def take_action(self, key_event: KeyEvent) -> None:
        """
        In each descendant, it will take the action according to the event.
        :param key_event: input from the user.
        :return: None
        """
        pass

    @abstractmethod
    def tick(self) -> bool:
        """
        For every tick itt will check the game state.
        :return: Returns a boolean variable during each timestep.
        """
        pass
