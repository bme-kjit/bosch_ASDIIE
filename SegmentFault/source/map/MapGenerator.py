"""
//*********************************************************************
//*********************************************************************
/ PROJECT_NAME : PacMan
/ FILENAME     : MapGenerator.py
/ AUTHOR       : Gergely Őri, Pal Lorand Juhasz, Bozsóki Márk
/ UNIVERSITY   : BME
/ TEAM         : SegmentFault
**********************************************************************
**********************************************************************
/ Short description
/ --------------------------------------------------------------------
/ Module is responsible for map generation

/*********************************************************************
/*********************************************************************
"""
import random

from source.map.MapData import MapData
from source.map.MapDataReader import MapDataReader
from source.map.MapElements import MapElements

class MapGenerator:
    def __init__(self):
        self.dataset = None


    def generate_mapdata(self, map_width: int, map_height: int) -> list[list[str]]:
        """ Generates the dataset for mapdata

        @args:
            map_width [int] - width of the dataset
            map_height [int] - height of the dataset
        @returns:
            dataset [list(list(str))] - the empty dataset
        """

        self.dataset = self.generate_empty_dataset(map_width, map_height)
        self.dataset = self.generate_border_of_walls()

        Player = self.get_random_coord()
        self.dataset[Player[0]][Player[1]] = MapElements.PacMan


    def generate_empty_dataset(self, width: int, height: int) -> list[list[str]]:
        """ Fills a concainer with MapElements.Place in th determined size
        
        @args:
            width [int] - width of the dataset
            height [int] - height of the dataset
        @returns:
            result [list(list(str))] - the empty dataset
        """

        result = []

        for x in range(0, width):
            result.append([])
            for y in range(0, height):
                result[x].append(MapElements.Place)
        
        return result
    

    def generate_border_of_walls(self) -> list[list[str]]:
        """ Generates border of wall in the dataset

        @returns:
            dataset [list(list(str))]
        """
        for i in range(len(self.dataset[0])):
            for j in range(len(self.dataset[1])):
                if i == 0 or i == len(self.dataset[0]):
                    self.dataset[i][j] = MapElements.Wall
                if j == 0 or j == len(self.dataset[1]):
                    self.dataset[i][j] = MapElements.Wall

        return self.dataset


    def get_random_coord(self) -> tuple[(int, int)]:
        """ Determines a random coordinate for MapElement placement from the available coordinates

        @returns:
            random_coord [tuple[(int, int)]] - the selected random coordinate
        """
        white_list = []

        for i in range(len(self.dataset[0])):
            for j in range(len(self.dataset[1])):
                if self.dataset[i][j] == MapElements.Place:
                    white_list.append((i,j))

        random_index = random.randint(0, (len(white_list) - 1))
        random_coord = white_list[random_index]

        return random_coord


    def fill_mapdata(self) -> MapData:
        """ Fills a MapData member with the generated dataset
        
        @returns:
            mapdata [MapData] - the generated mapdata
        """
        data_reader = MapDataReader()
        data_reader.data_set = self.dataset

        mapdata = data_reader.fill_mapdata()

        return mapdata