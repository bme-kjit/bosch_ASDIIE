import pygame

from Pybranch.core.wall_sprite import Wall
from Pybranch.core.screen_elements import Colors


class CreateWall:
    def __init__(self, colors: Colors):
        self.list_pos = int
        self.list_size = int
        self.wall_group = pygame.sprite.Group
        self.every_group = pygame.sprite.Group
        self.wall_pos_x = int
        self.wall_pos_y = int
        self.wall_size_width = int
        self.wall_size_height = int
        self.walls = pygame.sprite.Sprite
        self.colors = colors

    def create_wall(self, list_pos: tuple, list_size: tuple, wall_group: pygame.sprite.Group,
                    every_group: pygame.sprite.Group) -> None:
        """
            Create walls based on the tuples of positions and dimensions and added to the groups
        @args:
            list_pos [tuple] - tuple of wall positions
            list_size [tuple] - tuple of wall sizes
            wall_group [pygame.sprite.Group] - the group of walls
            every_group [pygame.sprite.Group] - the group of all sprites
        """
        self.list_pos = list_pos
        self.list_size = list_size
        self.wall_group = wall_group
        self.every_group = every_group
        for i in range(len(self.list_pos)):
            self.wall_pos_x = self.list_pos[i][0]
            self.wall_pos_y = self.list_pos[i][1]

            self.wall_size_width = self.list_size[i][0]
            self.wall_size_height = self.list_size[i][1]
            self.walls = Wall(self.wall_pos_x, self.wall_pos_y, self.wall_size_width, self.wall_size_height,
                              self.colors)

            self.wall_group.add(self.walls)
            self.every_group.add(self.walls)
