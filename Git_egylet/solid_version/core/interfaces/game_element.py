from abc import ABC, abstractmethod

from bosch_ASDIIE.Git_egylet.solid_version.core.enum.key_event import KeyEvent


class GameElement(ABC):
    @abstractmethod
    def take_action(self, key_event: KeyEvent):
        pass

    @abstractmethod
    def tick(self) -> bool:
        pass