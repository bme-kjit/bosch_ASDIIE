from enum import Enum
import pygame


class Constants(Enum):
    """
    Game-wide used constants
    """
    MAZE_SIZE_X = 10
    MAZE_SIZE_Y = 10
    WINDOW_HEIGHT = 600
    WINDOW_WIDTH = 600
    TILE_SIZE = WINDOW_HEIGHT / 10
    PACMAN_SIZE = TILE_SIZE / 2
    STEP_SIZE = TILE_SIZE
    COIN_SIZE = PACMAN_SIZE / 2
    COLOR_YELLOW = pygame.Color(255, 255, 0)
    COLOR_BLACK = pygame.Color(0, 0, 0)
    COLOR_WHITE = pygame.Color(255, 255, 255)
    COLOR_BLUE = pygame.Color(0, 0, 255)
    PACMAN_SPEED = 2
