"""
*********************************************************************
*********************************************************************
PROJECT_NAME : PacMan
FILENAME     : Movable.py
AUTHOR       : Juhász Pál Lóránd; Őri Gergely László; Seregi Bálint Leon; Bozsóki Márk
UNIVERSITY   : BME
TEAM         : SegmentFault
*********************************************************************
*********************************************************************
Short description
--------------------------------------------------------------------
Superclass for moving object in the game

********************************************************************
********************************************************************
"""

from source.dynamic_elements.Direction import Direction
from source.map.MapData import MapData
from source.map.MapElements import MapElements


class Movable():
    def __init__(self) -> None:
        pass
        
    def next_position(self, cur_position: tuple[int, int], direction: Direction) -> tuple[int, int]:
        """
        Calculates the next position based on the current position and the direction

        @args:
            cur_position [tuple(int, int)] - the current position
            dirertion [Direction]
        @return:
            (pos_x, pos_y) [int, int] - the next position
        """
        pos_x = cur_position[0]
        pos_y = cur_position[1]

        if direction == Direction.Right:
            pos_y += 1
        if direction == Direction.Down:
            pos_x += 1
        if direction == Direction.Left:
            pos_y -= 1
        if direction == Direction.Up:
            pos_x -= 1
        
        return (pos_x, pos_y)

    
    def last_position(self, cur_position: tuple[int, int], direction: Direction) -> tuple[int, int]:
        """
        Calculates the movalble object position last position based on thier direction
        
        @args:
            cur_position [tuple(int, int)] - the current position
            dirertion [Direction]
        @return:
            (pos_x, pos_y) [int, int] - the player last position
        """
        pos_x = cur_position[0]
        pos_y = cur_position[1]

        if direction == Direction.Right:
            pos_y -= 1
        if direction == Direction.Down:
            pos_x -= 1
        if direction == Direction.Left:
            pos_y += 1
        if direction == Direction.Up:
            pos_x += 1
            
        return (pos_x, pos_y)
    

    def jump_border(self, mapdata: MapData, cur_position: tuple[int, int]) -> tuple[int, int]:
        """
        Checks if the movable object reached the end of the map on any direction
        If the movable reaches the border, returns the moveables new position

        @args:
            mapdata [MapData]
            cur_position [tuple(int, int)] - the current position
            dirertion [Direction]
        @return:
            (pos_x, pos_y) [int, int] - the player new position
        """
        pos_x = cur_position[0]
        pos_y = cur_position[1]
        
        # check map bottom
        if pos_x == mapdata.height:
            pos_x = 0
        
        # check map top
        if pos_x < 0:
            pos_x = mapdata.height - 1
        
        # check map left
        if pos_y == mapdata.width:
            pos_y = 0

        # check map right
        if pos_y < 0:
            pos_y = mapdata.width - 1
        
        return (pos_x, pos_y)


    def what_is_ahead(self, mapdata: MapData, cur_position: tuple[int, int], direction: Direction) -> MapElements:
        """
        Returns the type of elemet is on the next position base on the current position and direction

        @args:
            mapdata [MapData]
            cur_position [tuple(int, int)] - the current position
            dirertion [Direction]
        @returns:
            element ahead [MapElement]
        """
        pos_x, pos_y = self.next_position(cur_position, direction)
        return mapdata[pos_x][pos_y]

        
    def is_wall_infront(self, mapdata: MapData, cur_position: tuple[int, int], direction: Direction) -> bool:
        """
        Determines if there is an obstacle (wall) on the next coordinate based on
        the given coordinates and direction

        @args:
            mapdata [MapData]
            cur_position [tuple(int, int)] - the current position
            dirertion [Direction]
        @return:
            True, if ther is an obstacle on the given coordinates
        """
        next_position = self.next_position(cur_position, direction)

        return next_position in mapdata.obstacles.walls