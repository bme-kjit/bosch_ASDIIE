from enum import Enum


class ActionEnum(Enum):
    """
    Constants for action selection.
    """
    UP = 'w'
    RIGHT = 'd'
    DOWN = 's'
    LEFT = 'a'


class MapEnum(Enum):
    """
    Constants for the map tiles.
    """
    AGENT_SLOT = '0'
    RESTRICTED_SLOT = '#'
    AWARD_SLOT = '-'
    TERMINATING_SLOT = 'X'
    EMPTY_SLOT = ' '
