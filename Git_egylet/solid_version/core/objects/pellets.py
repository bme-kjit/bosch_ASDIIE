from bosch_ASDIIE.Git_egylet.solid_version.core.interfaces.canvas import Canvas
from bosch_ASDIIE.Git_egylet.solid_version.core.enum.map import MapSize
from bosch_ASDIIE.Git_egylet.solid_version.core.interfaces.visualizable import Visualizable
from bosch_ASDIIE.Git_egylet.solid_version.core.interfaces.objects import Objects


class Pellets(Objects, Visualizable):
    """
    This class handles the creation and visualization of the pellets
    """
    def __init__(self,
                 map_size: MapSize = None,
                 number_pellets: int = 10,
                 ):
        if map_size is None:
            map_size = MapSize(10, 10)

        self.positions = self.make_objects(number=number_pellets, map_size=map_size)

    def draw(self, canvas: Canvas):
        """
        This function is responsible for the visualization of the pellets
        :param canvas: The interface for visualization
        :return:
        """
        canvas.draw_dots(self.positions, 'pellets')