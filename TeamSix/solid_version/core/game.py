from TeamSix.solid_version.enums.direction import Direction
from TeamSix.solid_version.enums.constans import Constants
from maze import Maze
import pygame
from TeamSix.solid_version.display.drawingService import DrawingService
from time import sleep
import sys


class Game:
    def __init__(self):
        self.pacman = None
        self.maze = None
        pygame.display.init()
        pygame.font.init()
        pygame.display.set_caption('TeamSix Pacman')
        screen = pygame.display.set_mode(
            (Constants['WINDOW_WIDTH'].value, Constants['WINDOW_HEIGHT'].value))
        screen.fill(Constants['COLOR_BLACK'].value)
        fps = pygame.time.Clock()
        self.start_game()
        self.drawing_service = DrawingService(screen)
        while not self.pacman.dead:
            self.pacman.has_moved = False
            self.handle_key_events()
            self.maze.step()
            self.maze.draw(self.drawing_service)
            self.pacman.draw(self.drawing_service)
            self.drawing_service.draw_score(self.pacman.points)
            pygame.display.update()
            fps.tick(Constants.PACMAN_SPEED.value)
        self.drawing_service.draw_game_over()
        pygame.display.update()
        sleep(5)

    def handle_key_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.pacman.direction = Direction.UP.value
                if event.key == pygame.K_DOWN:
                    self.pacman.direction = Direction.DOWN.value
                if event.key == pygame.K_LEFT:
                    self.pacman.direction = Direction.LEFT.value
                if event.key == pygame.K_RIGHT:
                    self.pacman.direction = Direction.RIGHT.value

    def start_game(self):
        self.maze = Maze()
        self.maze.init()
        self.pacman = self.maze.place_pacman(1, 1)


if __name__ == '__main__':
    sys.path.insert(0, '')
    game = Game()
    # game.start_game()
    # print(game.maze)
