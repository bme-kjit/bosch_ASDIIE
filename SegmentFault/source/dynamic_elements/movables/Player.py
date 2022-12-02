"""
//*********************************************************************
//*********************************************************************
/ PROJECT_NAME : PacMan
/ FILENAME     : Player.py
/ AUTHOR       : Márk Bozsóki
/ UNIVERSITY   : BME
/ TEAM         : SegmentFault
**********************************************************************
**********************************************************************
/ Short description
/ --------------------------------------------------------------------
/ Module responsible for movement and gameplay data

/*********************************************************************
/*********************************************************************
"""

from source.dynamic_elements.movables import Movable
from source.dynamic_elements.Direction import Direction
from source.map.MapData import MapData

class Player(Movable.Movable):
    def __init__(self, mapdata: MapData, start_position: tuple[int, int], start_direction: Direction):
        super().__init__()
        self.mapdata = mapdata
        self.position = start_position
        self.direction = start_direction
        self.next_direction = None

        self.is_dead = False
        self.score = 0


    def get_next_position(self) -> tuple[int, int]:
        """
        Sets the players new position based on the mapdata, current position and direction
        
        @return:
            (pos_x, pos_y) [int, int] - the player new position
        """

        # change the direction, if turning is available
        if self.next_direction != None:
            test_position = self.next_position(self.position, self.next_direction)
            if not self.is_wall_infront(self.mapdata, test_position, self.direction):
                self.direction = self.next_direction
                self.next_direction = None
        
        # calculate the next position
        self.position = self.next_position(self.position, self.direction)

        # reset position if obstacle ahead
        if self.is_wall_infront(self.mapdata, self.position, self.direction):
            pos_x, pos_y = self.last_position(self.position, self.direction)

        # jump to the other side
        pos_x, pos_y = self.jump_border(self.mapdata, self.position)

        return (pos_x, pos_y)


    def set_score(self):
        """
        Returns the score value on the player current position

        @return:
            score [int] - the value of the reward on the given coordinates
        """

        pos_x = self.position[0]
        pos_y = self.position[1]

        # check for points
        if (pos_x, pos_y) in self.mapdata.collectables.points:
            self.mapdata.collectables.points.remove((pos_x, pos_y))
            return 10

        # check for coins
        if (pos_x, pos_y) in self.mapdata.collectables.coins:
            self.mapdata.collectables.coins.remove((pos_x, pos_y))
            return 20

        #TODO: check for cherry

        #TODO: check for ghosts

        return 0