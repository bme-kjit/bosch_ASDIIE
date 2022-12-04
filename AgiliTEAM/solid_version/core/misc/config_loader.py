import os
from argparse import Namespace
import yaml
from typing import List

from core.misc.map import Coordinates


class ConfigLoader:

    def __init__(self, file_name):
        """
        The constructor of the config loader.
        :param file_name: name of the file.
        """
        self.file_name = file_name

    def load_config(self) -> Namespace:
        """
        It loads the config from a given path.
        :return: Returns the loaded config.
        """
        path = os.path.abspath(self.file_name)
        with open(path) as file:
            conf_dict = yaml.load(file, Loader=yaml.FullLoader)

        conf_dict['internal_walls'] = self.get_internal_walls_coordinates(conf_dict['internal_walls'])

        return Namespace(**conf_dict)

    @staticmethod
    def get_internal_walls_coordinates(coordinates_list: list) -> List[Coordinates]:
        """
        Gets the internal walls coordinates from the config
        :return: Returns the internal walls coordinates.
        """
        pos_list = []
        for coordinate_pair in coordinates_list:
            pos_list.append(Coordinates(coordinate_pair[0], coordinate_pair[1]))

        return pos_list
