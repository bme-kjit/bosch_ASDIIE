import pygame.sprite

from Pybranch.core.create_wall import CreateWall


class InnerWall:
    def __init__(self, wall: CreateWall) -> None:
        self.pos_list = ((150, 100), (150, 200), (550, 200), (850, 100), (100, 700), (250, 700), (600, 700), (750, 700))
        self.size_list = ((10, 200), (300, 10), (300, 10), (10, 200), (300, 10), (10, 200), (300, 10), (10, 200))
        self.wall = wall

    def create_wall(self, wall_sprites: pygame.sprite.Group,  every_sprites: pygame.sprite.Group):
        """
            Create the inner walls based on the lists of positions and dimensions by calling the create_wall function
        """
        self.wall.create_wall(self.pos_list, self.size_list, wall_sprites,
                              every_sprites)
