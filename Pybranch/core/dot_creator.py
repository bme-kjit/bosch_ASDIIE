import pygame

from Pybranch.core.collide import Collide
from Pybranch.core.list import ListToBool
from Pybranch.core.dot_sprite import Dot


class DotCreator:
    def __init__(self, collide: Collide, list_to_bool: ListToBool) -> None:
        self.collide = collide
        self.bool = list_to_bool

        self.sprite_number = int
        self.sprite = pygame.sprite.Sprite
        self.sprite_wall_collide_list = list
        self.sprite_wall_collide = bool
        self.sprite_dot_collide_list = list
        self.sprite_dot_collide = bool

    def dot_creator(self, sprite_number: int, wall_sprite: pygame.sprite.Group,  dots_sprite: pygame.sprite.Group,
                    every_sprite: pygame.sprite.Group) -> None:
        """
            Create an appropriate number of dots so that they do not conflict with the walls and other dots

        @args:
            sprite_number [int] - the number of dots to create
            wall_sprite [pygame.sprite.Group] - the group of Wall sprites
            dots_sprite [pygame.sprite.Group] - the group of Dot sprites
            every_sprite [pygame.sprite.Group] - the group of every sprite
        """

        self.sprite_number = sprite_number

        i = 0
        while i != sprite_number:
            self.sprite = Dot()
            self.sprite_wall_collide_list = self.collide.sprite_group_collision(self.sprite, wall_sprite, False)
            self.sprite_wall_collide = self.bool.list_checker(self.sprite_wall_collide_list)
            self.sprite_dot_collide_list = self.collide.sprite_group_collision(self.sprite, dots_sprite,
                                                                               False)
            self.sprite_dot_collide = self.bool.list_checker(self.sprite_dot_collide_list)
            if self.sprite_wall_collide is False and self.sprite_dot_collide is False:
                i += 1
                dots_sprite.add(self.sprite)
                every_sprite.add(self.sprite)
