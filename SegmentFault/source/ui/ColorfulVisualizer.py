"""
//*********************************************************************
//*********************************************************************
/ PROJECT_NAME : PacMan
/ FILENAME     : ColorfulVisualizer.py
/ AUTHOR       : Márk Bozsóki
/ UNIVERSITY   : BME
/ TEAM         : SegmentFault
**********************************************************************
**********************************************************************
/ Short description
/ --------------------------------------------------------------------
/ Module for rendering colorful map

/*********************************************************************
/*********************************************************************
"""
import cv2
import numpy as np
from source.map.MapData import MapData

class ColorfulVisualizer:
    def __init__(self, mapdata: MapData) -> None:
        self.mapdata = mapdata

        self.ratio = 10
        self.height = mapdata.height * self.ratio
        self.width = mapdata.width * self.ratio

        self.game_state = None
        self.rendered_image = None

    def refresh_game_state(self):
        """
        Creates a matrix with the current game state
        """
        pass

    def render_game_state(self):
        """
        Creates and displays a window with the current game state
        """
        pass

