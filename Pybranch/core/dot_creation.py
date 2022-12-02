import pygame
from Pybranch.core.dot_creator import DotCreator


class DotCreation:
    def __init__(self, dot: DotCreator) -> None:
        self.creation = dot
        self.dot_number = 60

    def dot_creation(self, wall_sprite: pygame.sprite.Group, dots_sprite: pygame.sprite.Group,
                     every_sprite: pygame.sprite.Group) -> None:
        """
            Create the points here by calling the dot_creator function

        @args:
            wall_sprite [pygame.sprite.Group] - the group of Wall sprites
            dots_sprite [pygame.sprite.Group] - the group of Dot sprites
            every_sprite [pygame.sprite.Group] - the group of every sprite
        """
        self.creation.dot_creator(self.dot_number, wall_sprite,  dots_sprite, every_sprite)

