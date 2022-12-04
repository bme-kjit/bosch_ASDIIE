import pygame
import sys
from pygame.locals import *

from Pybranch.core.game import Game
from Pybranch.gui.game_scene import GameScene
from Pybranch.core.pacman_sprite import PacMan
from Pybranch.core.move import Move
from Pybranch.core.sprite_draw import SpriteDraw
from Pybranch.core.collide import Collide
from Pybranch.core.list import ListToBool
from Pybranch.core.score import Score
from Pybranch.core.game_time import GameTime
from Pybranch.gui.screen import Screen
from Pybranch.core.screen_elements import Colors
from Pybranch.core.screen_elements import Font
from Pybranch.core.surface import Surface
from Pybranch.core.create_wall import CreateWall
from Pybranch.core.inner_wall import InnerWall
from Pybranch.core.border_wall import BorderWall
from Pybranch.core.dot_creation import DotCreation
from Pybranch.core.dot_creator import DotCreator
from Pybranch.core.screen_border_checking import ScreenBorderChecking

pygame.init()

# The game refresh rate
FPS = 60
FramePerSec = pygame.time.Clock()
Screen_Size = 1000


if __name__ == "__main__":
    surface = Surface(Screen_Size, Screen_Size)
    screen = Screen(Colors(), Font(), surface)
    dot_creator = DotCreator(Collide(), ListToBool())
    inner_wall = InnerWall(CreateWall(Colors()))
    border = BorderWall(CreateWall(Colors()))
    dot_creation = DotCreation(dot_creator)
    pacman = PacMan(Collide(), ListToBool())
    game_scene = GameScene(pacman, Score(), GameTime(), screen, inner_wall, border, dot_creation)
    move = Move(ScreenBorderChecking())
    draw = SpriteDraw(screen)
    game = Game(game_scene, pacman, move, draw)

    game.game_scene.starting_map()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        game.run()
        game.game_over()

        pygame.display.update()
        FramePerSec.tick(FPS)
