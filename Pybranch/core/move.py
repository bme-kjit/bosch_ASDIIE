import pygame
from pygame.locals import *

from Pybranch.core.screen_border_checking import ScreenBorderChecking


class Move:
    def __init__(self, border_checking: ScreenBorderChecking) -> None:
        self.speed = 5
        self.border_checking = border_checking
        self.screen_height = int
        self.screen_width = int
        self.sprite = pygame.sprite.Sprite

    def move(self, sprite: pygame.sprite.Sprite, screen_height: int, screen_width: int) -> None:
        """
            Moves the given sprite using the arrow keys

        @args:
            (screen_height, screen_width) [int, int] - the screen sizes
        """
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.sprite = sprite

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.sprite.rect.move_ip(0, -self.speed)

        elif pressed_keys[K_DOWN]:
            self.sprite.rect.move_ip(0, self.speed)

        elif pressed_keys[K_LEFT]:
            self.sprite.rect.move_ip(-self.speed, 0)

        elif pressed_keys[K_RIGHT]:
            self.sprite.rect.move_ip(self.speed, 0)
        self.border_checking.border_checking(self.sprite, self.screen_height, self.screen_width)
