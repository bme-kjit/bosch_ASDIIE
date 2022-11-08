"""
//*********************************************************************
//*********************************************************************
/ PROJECT_NAME : PacMan
/ FILENAME     : MapData.py
/ AUTHOR       : Márk Bozsóki
/ UNIVERSITY   : BME
/ TEAM         : SegmentFault
**********************************************************************
**********************************************************************
/ Short description
/ --------------------------------------------------------------------
/ Position data provider, from a local .dat file

/*********************************************************************
/*********************************************************************
"""

from source.map import MapElements

class MapData():
    def __init__(self) -> None:
        self.size = (0,0)
        self.width = self.size[0]
        self.height = self.size[1]

        self.obstacles = Obstacles()

        self.collectables = Collectables()

        self.enemies = Enemies()

        self.Player = (0,0)

class Obstacles():
    walls = []
    door = (0,0)

class Collectables():
    points = []
    coins = []
    #TODO: add cherry

class Enemies():
    Blinky = (0,0) # red ghost
    Pinky = (0,0)  # pink ghost
    Inky = (0,0)   # cyan ghost
    Clyde = (0,0)  # orange ghost