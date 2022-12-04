from enum import Enum


class KeyEvent(Enum):
    """
    Key events possibly detected while using the application
    """
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4