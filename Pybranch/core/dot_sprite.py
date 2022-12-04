import pygame
import random


class Dot(pygame.sprite.Sprite):
    def __init__(self) -> None:
        """
            Create a Dot sprite of the given size with random position
        """
        self.frame_min = 40
        self.frame_max = 960
        self.dot_size = (20, 20)
        # Loading the Dot from file and transform to the required size with random position

        super().__init__()
        self.image = pygame.image.load('dot.png')
        self.image = pygame.transform.scale(self.image, self.dot_size)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(self.frame_min, self.frame_max)
        self.rect.y = random.randint(self.frame_min, self.frame_max)
        