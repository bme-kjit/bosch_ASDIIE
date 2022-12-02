import pygame
from Pybranch.core.screen_elements import Colors


class Wall(pygame.sprite.Sprite):

    def __init__(self, left: int, top: int, width: int, height: int, colors: Colors) -> None:
        """
            Create a wall sprite of the given size and location
        @args:
            (left, top) [int, int] - position of the left side and the top of the wall to be created
            (width, height) [int,int] - the width and height of the wall to be created
        """
        self.width = width
        self.height = height
        self.color = colors
        super().__init__()
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color.blue)
        self.rect = self.image.get_rect()
        self.rect.x = left
        self.rect.y = top
