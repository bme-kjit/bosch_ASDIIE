import pygame.sprite

from Pybranch.core.create_wall import CreateWall


class BorderWall:
    def __init__(self, create_wall: CreateWall) -> None:
        self.pos_list = (
            (0, 0), (0, 0), (0, 990), (990, 0), (0, 550), (990, 550), (550, 0), (550, 990), (0, 450), (0, 550),
            (890, 450),
            (890, 550), (450, 0), (550, 0), (450, 890), (550, 890))
        self.size_list = (
            (10, 450), (450, 10), (450, 10), (10, 450), (10, 450), (10, 450), (450, 10), (450, 10), (100, 10),
            (100, 10),
            (110, 10), (100, 10), (10, 100), (10, 100), (10, 110), (10, 100))
        self.wall = create_wall

    def create_wall(self, wall_sprites: pygame.sprite.Group,  every_sprites: pygame.sprite.Group):
        """
            Create the border walls based on the lists of positions and dimensions by calling the create_wall function
        """
        self.wall.create_wall(self.pos_list, self.size_list, wall_sprites,
                              every_sprites)
