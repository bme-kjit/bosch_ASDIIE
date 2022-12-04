from typing import Union, Any
from collections import namedtuple
from Objects.core.maps.map_descriptior import association

#actual position of pacman
Coordinates = namedtuple("Coordinates", ("row", "col"))


class MapVariation:
    def __init__(self, map_name: str = "map1"):
        """
        Class for map management.
        :param map_name(str): map name
        """
        self.map_path = f"Objects/core/maps/{map_name}.txt"
        self.map = self._load_map()

    def get_map(self):
        """
        Returns the loaded text map.
        :return (list): text format of map
        """
        return self.map

    def _load_map(self):
        """Loads the map from .txt file."""
        with open(self.map_path, "r") as f:
            lines = f.readlines()
        
        # remove \n form line ends
        lines = [line[:-1] for line in lines]
        return lines

    def get_annotation(self, object_type: str):
        """Returns the annotation of a map object."""
        return association[object_type]
    
    @property
    def pacman_start_position(self):
        """Returns pacman start position."""
        coords = self._get_coordinates_of_objects("pacman")[0]
        return Coordinates(coords[0], coords[1])
        
    @property
    def wall_positions(self):
        """Returns the wall positions."""
        return self._get_coordinates_of_objects("wall")

    @property
    def ghost_positions(self):
        """Returns the ghost positions."""
        ghost_positions = [Coordinates(coord[0], coord[1]) 
            for coord in self._get_coordinates_of_objects("ghost")]
        return ghost_positions
    
    @property
    def food_positions(self):
        """Returns the food positions."""
        food_positions = [Coordinates(coord[0], coord[1]) 
            for coord in self._get_coordinates_of_objects("food")]
        return food_positions


    def _indexlist(self, list_or_string: Union[list, str], item2find: Any):
        "Returns all indexes of an item in a list or a string"
        return [n for n,item in enumerate(list_or_string) if item==item2find]

    def _get_coordinates_of_objects(self, object_type: str):
        """Returns the coordinates of the asked oject type on the map."""
        found_positions = []
        for row, map_line in enumerate(self.map):
            line_pos = self._indexlist(map_line, self.get_annotation(object_type))
            if len(line_pos) > 0:
                found_positions += [(row, col) for col in line_pos]
        return found_positions

    def _remove_element_from_map(self, coordiante: Coordinates):
        """Removes element form map."""
        line = list(self.map[coordiante.row])
        line[coordiante.col] = " "
        self.map[coordiante.row] = "".join(line)
        
        