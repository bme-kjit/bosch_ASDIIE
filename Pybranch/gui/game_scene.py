import pygame
from Pybranch.core.pacman_sprite import PacMan
from Pybranch.core.score import Score
from Pybranch.core.game_time import GameTime
from Pybranch.gui.screen import Screen
from Pybranch.core.inner_wall import InnerWall
from Pybranch.core.border_wall import BorderWall
from Pybranch.core.dot_creation import DotCreation


class GameScene:
    def __init__(self, pacman: PacMan, score: Score, game_time: GameTime, screen: Screen, inner_wall: InnerWall,
                 border: BorderWall, dot: DotCreation) -> None:
        self.current_time = float
        self.current_score = int
        self.game_time = float
        self.pacman = pacman
        self.screen = screen
        self.score = score
        self.time = game_time
        self.inner_wall = inner_wall
        self.border = border
        self.dot = dot
        self.pacman_dot_collision_list = self.pacman.collide.sprite_group_collision(self.pacman, self.screen.dots, True)
        self.dots = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.every_sprites = pygame.sprite.Group()
        self.game_over_pos_x = 320
        self.game_over_pos_y = 500
        self.game_over = self.screen.font.font.render("Game Over", True, self.screen.color.yellow)

    def starting_map(self) -> None:
        """
            Create the starting map
        """
        self.screen.starting_window_creation()
        self.border.create_wall(self.walls, self.every_sprites)
        self.inner_wall.create_wall(self.walls, self.every_sprites)
        self.dot.dot_creation(self.walls, self.dots, self.every_sprites)

    def game_scene(self) -> None:
        """
            Show the game scene
        """
        self.game_time = self.time.game_time_counting()
        self.score.score = self.score.score_increase(self.screen.dots, self.pacman_dot_collision_list)
        self.screen.surface.DISPLAYSURF.fill(self.screen.color.black)
        self.current_score = self.screen.font.font_small.render(str(self.score.score), True, self.screen.color.white)
        self.current_time = self.screen.font.font_small.render(str(self.game_time), True, self.screen.color.white)
        self.screen.surface.DISPLAYSURF.blit(self.current_score, (self.score.score_pos, self.score.score_pos))
        self.screen.surface.DISPLAYSURF.blit(self.current_time, (self.time.time_pos_x, self.time.time_pos_y))

    def game_over_scene(self) -> None:
        """
            Show the game over scene
        """
        self.screen.surface.DISPLAYSURF.fill(self.screen.color.black)
        self.screen.surface.DISPLAYSURF.blit(self.game_over, (self.game_over_pos_x, self.game_over_pos_y))
