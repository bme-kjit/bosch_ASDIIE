import pygame


class GameTime:
    def __init__(self) -> None:
        self.game_time = float
        self.time_pos_x = 930
        self.time_pos_y = 20
        self.max_time = 60000

    def game_time_counting(self) -> float:
        """
            Sets the remaining game time
        @return:
            game_time [float]-the remaining game time
        """
        self.game_time = round(((self.max_time - pygame.time.get_ticks()) / 1000), 2)
        return self.game_time
