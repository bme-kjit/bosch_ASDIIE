import pygame


class Colors:
    def __init__(self) -> None:
        """
            The variables of the colors used in the program
        """
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.yellow = (255, 255, 0)
        self.blue = (0, 0, 255)


class Font:
    def __init__(self) -> None:
        """
            The variables of fonts used in the program
        """
        self.font_size = 60
        self.font_size_small = 20
        self.font = pygame.font.SysFont("Verdana", self.font_size)
        self.font_small = pygame.font.SysFont("Verdana", self.font_size_small)
