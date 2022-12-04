import pygame


class Surface:
    def __init__(self, screen_size_width: int, screen_size_height: int) -> None:
        """
            Create a surface of the given size
        @args:
            (screen_height, screen_width) [int, int]-the screen sizes
        """
        self.screen_size_width = screen_size_width
        self.screen_size_height = screen_size_height
        self.DISPLAYSURF = pygame.display.set_mode((self.screen_size_width, self.screen_size_height))
