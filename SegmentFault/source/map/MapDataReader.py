"""
//*********************************************************************
//*********************************************************************
/ PROJECT_NAME : PacMan
/ FILENAME     : MapDataReader.py
/ AUTHOR       : Gergely Őri, Bozsóki Márk
/ UNIVERSITY   : BME
/ TEAM         : SegmentFault
**********************************************************************
**********************************************************************
/ Short description
/ --------------------------------------------------------------------
/ Data provider, from selected local .mapdat files

/*********************************************************************
/*********************************************************************
"""

import os
from pathlib import Path

from source.map.MapData import MapData
from source.map.MapElements import MapElements

class MapDataReader:

    def __init__(self) -> None:
        self.data_set = []

    @staticmethod
    def list_mapdatas() -> list[str]:
        """ Gathers the available .mapdat filenames

        @returns:
            mapdata_files [list(str)]
        """
        mapdata_files = []

        current_dir = os.path.dirname(__file__)
        parent_dir = Path(current_dir).parent.parent.absolute()
        mapdata_dir = os.path.join(parent_dir, "data/maps")
        for mapdat in os.listdir(mapdata_dir):
            mapdata_files.append(os.path.join(mapdata_dir, mapdat))
        
        return mapdata_files

    def load_mapdata(self, map: str) -> list[list[str]]:
        """ Loads the mapdata from the file of the given path as lol(str)

        @args:
            self
            mapdatafile_path [str] - path for the mapdata file
        @return:
            dataset [List[List[str]]] - list of list containing the mapdata
        """

        index = 0
        if not map is None:
            mapdata_paths = self.list_mapdatas()
            for item in mapdata_paths:
                # if the path contains the map string
                if item.find(map) != -1:
                    mapdatafile_path = mapdata_paths[index]
                index += 1

        mapdata = open(mapdatafile_path, 'r')

        while True:
            line = mapdata.readline()

            # EndOfFile
            if not line:
                break

            if list(line)[-1] == '\n':
                self.data_set.append(list(line)[:-1])
            else:
                self.data_set.append(list(line))

        mapdata.close()

        return self.data_set


    def fill_mapdata(self) -> MapData:
        """ Fills a MapData member with mapdata

        
        @returns:
            mapdata [MapData] - class member holding the mapdata
        """

        # init MapData
        mapdata = MapData()
        mapdata.size = self.get_size()
        mapdata.width = mapdata.size[0]
        mapdata.height = mapdata.size[1]

        # get obstacles start position
        if self.contains(MapElements.Wall):
            mapdata.obstacles.walls = self.get_coords_of(MapElements.Wall)
        
        if self.contains(MapElements.Door):
            mapdata.obstacles.door = self.get_first_coord_of(MapElements.Door)

        # get collectables start position
        if self.contains(MapElements.Coin):
            mapdata.collectables.coins = self.get_coords_of(MapElements.Coin)

        if self.contains(MapElements.Point):
            mapdata.collectables.points = self.get_coords_of(MapElements.Point)
        
        #TODO: add cherry

        # get enemies start position
        if self.contains(MapElements.Blinky):
            mapdata.enemies.Blinky = self.get_first_coord_of(MapElements.Blinky)
        
        if self.contains(MapElements.Clyde):
            mapdata.enemies.Clyde = self.get_first_coord_of(MapElements.Clyde)
        
        if self.contains(MapElements.Inky):
            mapdata.enemies.Inky = self.get_first_coord_of(MapElements.Inky)

        if self.contains(MapElements.Pinky):
            mapdata.enemies.Pinky = self.get_first_coord_of(MapElements.Pinky)

        # get player start position
        if self.contains(MapElements.PacMan):
            mapdata.Player = self.get_first_coord_of(MapElements.PacMan)

        return mapdata
        

    def get_size(self) -> tuple[(int, int)]:
        """ Determines the loaded mapsize

        @args:
            self
        @return:
            size [tuple(int, int)] - [0] - width of the map
                                     [1] - height of the map
        """
        map_height = len(self.data_set)
        map_width = 0

        for i in self.data_set:
            map_width = len(i)

        return (map_width, map_height)



    def contains(self, element: MapElements) -> bool:
        """ Determines if the dataset contains the given MapElement
        
        @args:
            self,
            element [MapElement] - the given MapElement
        @return:
            result [bool] - True, if the mapdata contains the given MapElement
        """
        for i in range(len(self.data_set)):
            if element in self.data_set[i]:
                return True

        return False


    def get_first_coord_of(self, element: MapElements) -> tuple[(int, int)]:
        """ Returns the coordinates of the given MapElement
        
        @args:
            self,
            element [MapElement] - the given MapElement
        @returns:
            result [tuple(x [int], y [int])] - the first found coordinate          
        """
        if not self.contains(element):
            raise Exception(f"The Map does not contain the given MapElement: {element.name} {element.value}")

        x = 0
        y = 0
        
        for i in range(len(self.data_set)):

            y = 0
            for j in self.data_set[i]:
                if j == element.value:
                    return (x,y)
                y += 1

            x +=1
        

    def get_coords_of(self, element: MapElements) -> list[(int,int)]:
        """ Returns a list of coordinates as tuple of the given MapElement
        
        @args:
            self,
            element [MapElement] - the given MapElement
        @returns:
            result [list[tuple(int,int)]] - the found coordinates on the map
        """
        if not self.contains(element):
            raise Exception(f"The Map does not contain the given MapElement: {element.name} {element.value}")

        result = []
        x = 0
        y = 0
        
        for i in range(len(self.data_set)):

            y = 0
            for j in self.data_set[i]:
                if j == element.value:
                    result.append((x,y))
                y += 1

            x +=1

        return result
