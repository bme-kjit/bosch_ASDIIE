import pygame
from Pybranch.gui.screen import Screen


class SpriteDraw:
    def __init__(self, screen: Screen) -> None:
        self.any_sprite = pygame.sprite.Sprite
        self.screen = screen

    def sprite_draw(self, any_sprite: pygame.sprite.Group) -> None:
        """
            Display a group on the screen
        @args:
            any_sprite [pygame.sprite.Group]- group to be displayed
        """
        self.any_sprite = any_sprite
        self.any_sprite.draw(self.screen.surface.DISPLAYSURF)
