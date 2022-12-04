import pygame


class Score:
    def __init__(self) -> None:
        self.hit_list = list
        self.sprite_group = pygame.sprite.Group
        self.score_pos = 20
        self.score = 0

    def score_increase(self, sprite_group: pygame.sprite.Group, hit_list: list) -> int:
        """
            Increase the score
        @args:
            any_sprite [pygame.sprite.Group] - group that is worth points
            hit_list [list] - list containing the sprites the player picked up
        @return:
            self.score [int] - actual score
        """
        self.sprite_group = sprite_group
        self.hit_list = hit_list

        for self.sprite_group in self.hit_list:
            self.score += 1
        return self.score
