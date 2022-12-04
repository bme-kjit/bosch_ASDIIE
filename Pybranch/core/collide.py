import pygame


class Collide:

    def __init__(self):
        self.sprite = pygame.sprite.Sprite
        self.group = pygame.sprite.Group
        self.kill = bool

    def sprite_group_collision(self, sprite: pygame.sprite.Sprite, group: pygame.sprite.Group, kill: bool) -> list:
        """
            Create a list of sprites from the group that collide with the another sprite
        @args:
            sprite [pygame.sprite.Sprite] - the sprite to be tested for collision
            group [pygame.sprite.Group] - the group to be tested for collision
            kill [bool] - remove or not remove from the group
        @return:
            hit_list [list] - list containing the sprites that collided with the other sprite
        """
        self.sprite = sprite
        self.group = group
        self.kill = kill
        hit_list = pygame.sprite.spritecollide(self.sprite, self.group, self.kill)
        return hit_list
