from abc import ABC, abstractmethod

from Objects.core.get_action import KeyEvent


class GameElement(ABC):
    @abstractmethod
    def take_action(self, key_event: KeyEvent):
        pass

    @abstractmethod
    def tick(self) -> bool:
        pass