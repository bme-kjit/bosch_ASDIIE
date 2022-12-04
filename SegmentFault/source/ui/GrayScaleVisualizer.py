"""
//*********************************************************************
//*********************************************************************
/ PROJECT_NAME : PacMan
/ FILENAME     : GrayScaleVisualizer.py
/ AUTHOR       : Márk Bozsóki
/ UNIVERSITY   : BME
/ TEAM         : SegmentFault
**********************************************************************
**********************************************************************
/ Short description
/ --------------------------------------------------------------------
/ Module for rendering grayscale map

/*********************************************************************
/*********************************************************************
"""
import cv2
import numpy as np
from source.map.MapData import MapData

class GrayScaleVisualizer():
    def __init__(self, size_ratio: int, ) -> None:
        self.ratio = size_ratio
        
        self.game_state = None

        # color values
        self.player_color = 1
        self.ghost_color = 0.75
        self.door_color = 0.55
        self.wall_color = 0.45
        self.point_color = 0.25
        self.coin_color = 0.35

    def refresh_game_state(self, mapdata: MapData) -> None:
        """
        Creates a matrix with the current game state
        """
        self.game_state = np.zeros((mapdata.size[1], mapdata.size[0], 1))

        # add player
        self.game_state[mapdata.Player[0], mapdata.Player[1], 0] = self.player_color

        # add obstacles
        # walls
        for coord in mapdata.obstacles.walls:
            self.game_state[coord[0], coord[1], 0] = self.wall_color
        
        # door
        self.game_state[mapdata.obstacles.door[0], mapdata.obstacles.door[1], 0] = self.door_color

        # add collectables
        # points
        for coord in mapdata.collectables.points:
            self.game_state[coord[0], coord[1], 0] = self.point_color
        
        # coins
        for coord in mapdata.collectables.coins:
            self.game_state[coord[0], coord[1], 0] = self.coin_color

        #TODO: add enemies


    def render_game_state(self, map_size: tuple[int,int]) -> None:
        """
        """
        if self.game_state is not None:
            image = np.float32(self.game_state)
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

            height = map_size[1] * self.ratio
            width = map_size[0] * self.ratio
            rendered_image = np.zeros((height, width, 3))

            # rescale original image from the grid world to visualize with OpenCv
            for h in range(height):
                for w in range(width):
                    rendered_image[h][w] = image[h // self.ratio][w // self.ratio]
            
            # show window
            cv2.imshow("SegmentFault's PacMan", rendered_image)

            # add wait to see the game
            cv2.waitKey(50)