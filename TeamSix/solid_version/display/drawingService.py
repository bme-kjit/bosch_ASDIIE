import pygame
from TeamSix.solid_version.enums.constans import Constants


class DrawingService:

    def __init__(self, screen):
        self.screen = screen

    def draw_field(self, tile_position_x, tile_position_y, field_type):
        if field_type == 'WALL':
            color = Constants.COLOR_BLUE.value
        else:
            color = Constants.COLOR_BLACK.value
        pygame.draw.rect(self.screen, color, pygame.Rect(tile_position_x * Constants.TILE_SIZE.value,
                                                         tile_position_y * Constants.TILE_SIZE.value,
                                                         Constants.TILE_SIZE.value, Constants.TILE_SIZE.value))

    def draw_coin(self, tile_position_x, tile_position_y):
        # x,y are the index of the field, multiplying with field size gives the top left coordinates on the screen
        # convert it to the middle, since circle drawing requires that
        circle_x = tile_position_x * Constants.TILE_SIZE.value + Constants.TILE_SIZE.value / 2
        circle_y = tile_position_y * Constants.TILE_SIZE.value + Constants.TILE_SIZE.value / 2
        pygame.draw.circle(self.screen, Constants.COLOR_WHITE.value, (circle_x, circle_y), Constants.COIN_SIZE.value)

    def draw_pacman(self, tile_position_x, tile_position_y):
        # x,y are the index of the field, multiplying with field size gives the top left coordinates on the screen
        # convert it to the middle, since circle drawing requires that
        circle_x = tile_position_x * Constants.TILE_SIZE.value + Constants.TILE_SIZE.value / 2
        circle_y = tile_position_y * Constants.TILE_SIZE.value + Constants.TILE_SIZE.value / 2
        pygame.draw.circle(self.screen, Constants.COLOR_YELLOW.value, (circle_x, circle_y), Constants.PACMAN_SIZE.value)

    def draw_score(self, score):
        font = pygame.font.SysFont('Comic Sans MS', 12)
        text = font.render('Score: ' + str(score), False, Constants.COLOR_WHITE.value)
        self.screen.blit(text, (5, 5))

    def draw_game_over(self,):
        font = pygame.font.SysFont('Comic Sans MS', 22)
        text = font.render('Game over!', False, Constants.COLOR_WHITE.value)
        self.screen.blit(text, (Constants.WINDOW_WIDTH.value/2-50, Constants.WINDOW_HEIGHT.value/2))
