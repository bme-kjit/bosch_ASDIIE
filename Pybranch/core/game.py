import time
import pygame
import sys
from Pybranch.gui.game_scene import GameScene
from Pybranch.core.pacman_sprite import PacMan
from Pybranch.core.move import Move
from Pybranch.core.sprite_draw import SpriteDraw


class Game:
    def __init__(self, game_scene: GameScene, pacman: PacMan, move: Move, draw: SpriteDraw) -> None:
        self.game_scene = game_scene
        self.pacman = pacman
        self.move = move
        self.draw = draw
        self.over = bool
        self.pacman_wall_collision_list = self.pacman.collide.sprite_group_collision(
            self.pacman, self.game_scene.walls, False)
        self.pacman_wall_collision = self.pacman.bool.list_checker(self.pacman_wall_collision_list)
        self.game_scene.pacman_dot_collision_list = self.pacman.collide.sprite_group_collision(
            self.pacman, self.game_scene.dots, True)
        self.game_scene.every_sprites.add(self.pacman)

    def run(self) -> None:
        """
            Call the functions needed to run the game
        """
        self.game_scene.game_scene()
        self.move.move(self.pacman, self.game_scene.screen.screen_size, self.game_scene.screen.screen_size)
        self.pacman_wall_collision_list = self.pacman.collide.sprite_group_collision(
            self.pacman, self.game_scene.walls, False)
        self.pacman_wall_collision = self.pacman.bool.list_checker(self.pacman_wall_collision_list)
        self.game_scene.pacman_dot_collision_list = self.pacman.collide.sprite_group_collision(
            self.pacman, self.game_scene.dots, True)
        self.draw.sprite_draw(self.game_scene.every_sprites)

    def is_it_over(self, score: int, dot_number: int, game_time: [float], collision: bool) -> bool:
        """
            Checks if the game is not over
        @args:
            score [int] - the game score
            dot_number [int] - the number of dots
            game_time [float] - the time available to play
            collision [bool] - whether there was a collision
        """

        if score == dot_number or game_time <= 0.0 or collision is True:
            return True
        else:
            return False

    def game_over(self):
        self.over = self.is_it_over(self.game_scene.score.score, self.game_scene.dot.dot_number,
                                    self.game_scene.game_time, self.pacman_wall_collision)
        if self.over is True:
            time.sleep(0.5)
            self.game_scene.game_over_scene()
            pygame.display.update()
            for entity in self.game_scene.every_sprites:
                entity.kill()
            time.sleep(2)
            pygame.quit()
            sys.exit()
