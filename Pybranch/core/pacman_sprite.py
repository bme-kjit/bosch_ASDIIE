import pygame
from Pybranch.core.list import ListToBool
from Pybranch.core.collide import Collide


class PacMan(pygame.sprite.Sprite):
    def __init__(self, collide: Collide, list_to_bool: ListToBool) -> None:
        """
            Create a PacMan sprite of the given size and location
        """
        self.pos_x = 160
        self.pos_y = 520
        self.size = (50, 50)
        self.collide = collide
        self.bool = list_to_bool

        super().__init__()
        self.image = pygame.image.load("Pacman.png")
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)
