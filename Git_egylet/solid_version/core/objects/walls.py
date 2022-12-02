from bosch_ASDIIE.Git_egylet.solid_version.core.interfaces.canvas import Canvas
from bosch_ASDIIE.Git_egylet.solid_version.core.enum.map import MapSize
from bosch_ASDIIE.Git_egylet.solid_version.core.interfaces.visualizable import Visualizable
from bosch_ASDIIE.Git_egylet.solid_version.core.interfaces.objects import Objects


class Walls(Objects, Visualizable):
    """
    This class is responsible for the creation and visualization of the walls
    """
    def __init__(self,
                 map_size: MapSize = None,
                 number_walls: int = 10,
                 ):
        if map_size is None:
            map_size = MapSize(10, 10)

        self.positions = self.make_objects(number=number_walls, map_size=map_size)

    def draw(self, canvas: Canvas):
        """
        This class is responsible for the visualization of the walls
        :param canvas: The interface for visualization
        :return:
        """
        canvas.draw_dots(self.positions, 'walls')