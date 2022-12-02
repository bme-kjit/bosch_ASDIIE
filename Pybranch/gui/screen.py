import pygame

from Pybranch.core.screen_elements import Colors
from Pybranch.core.screen_elements import Font
from Pybranch.core.surface import Surface


class Screen:
    def __init__(self, colors: Colors, font: Font, surface: Surface) -> None:
        self.time_pos = 930
        self.color = colors
        self.surface = surface
        self.screen_size = self.surface.screen_size_width
        self.font = font
        self.dots = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.every_sprites = pygame.sprite.Group()

    def starting_window_creation(self) -> None:
        """
            Show the start of the game scene
        """
        self.surface.DISPLAYSURF.fill(self.color.black)
        pygame.display.set_caption("PACMAN")
