"""
*********************************************************************
*********************************************************************
PROJECT_NAME : PacMan
FILENAME     : PacMan.py
AUTHOR       : Juhász Pál Lóránd; Őri Gergely László; Seregi Bálint Leon; Bozsóki Márk
UNIVERSITY   : BME
TEAM         : SegmentFault
*********************************************************************
*********************************************************************
Short description
--------------------------------------------------------------------
Ghosts object definitions, movement and modes

********************************************************************
********************************************************************
"""

import Movable, Direction, GhostMode
from source.map.MapData import MapData

class Ghost(Movable):
    def __init__(self, mapdata: MapData, start_position: tuple[int, int]) -> None:
        super().__init_()
        self.mapdata = mapdata
        self.position = start_position
        self.last_position = start_position
        self.direction = self.generate_new_direction()
        self.safehouse_position = self.get_safehouse_position()

        self.mode = GhostMode.Roam
        self.path = []

    def get_safehouse_position(self):
        """
        Calculates the first position on the map next to the Door
        where the Player can't reach the Ghost
        """
        pass


    def generate_new_direction(self):
        """
        Generates a random direction for the Ghost member based on mapdata
        """
        pass
        


    def set_next_position(self):
        """
        Calculates the Ghost next position based on the GhostMode
        """
        # goes around the map with no bad intention
        if self.mode == GhostMode.Roam:
            #TODO: calculate next position and direction
            
            #TODO: change Ghostmode as the Player visible and exit the if statment
            
            #TODO: append next position to path
            self.path = []
            self.path.append(0,0)

        # if saw the player, goes to the last position where the player was seen
        if self.mode == GhostMode.Hunt:
            if self.is_PacMan_visible():
                self.path = self.calculate_path_to(self.mapdata.Player)

        # if the player eats a coin the Ghost goes to the safehouse position
        if self.mode == GhostMode.Fear:
            if self.path[-1] != self.safehouse_position:
                self.path = self.calculate_path_to(self.safehouse_position)
            
            if self.position == self.safehouse_position:
                self.mode = GhostMode.Roam

        # moves to next position
        self.position = self.path[0]
        self.path.remove[0]

        #TODO: refresh direction as the Ghost move on its path

    
    def is_PacMan_visible(self) -> bool:
        """
        Determines if PacMan is visible for the Ghost

        @return:
            True, if PacMan is in the way of the Ghost
        """
        
        test_pos_x = self.position[0]
        test_pos_y = self.position[1]
        test_position = (test_pos_x, test_pos_y)

        while not super().is_wall_ahead(self.mapdata, test_position, self.direction):
            test_position = super().next_position(test_position, self.direction)
            if self.mapdata.Player == test_position:
                return True

        return False

    def calculate_path_to(self, destination: tuple[int, int]) -> list[tuple[int, int]]:
        """
        Calculates the shortest path from the current position to the destination

        @args:
            destination [tuple(int, int)]
        @returns:
            path [list(tuple(int, int))]
        """
        self.path = []

        #TODO: implement shortest path search

