from typing import List

from bosch_ASDIIE.Git_egylet.solid_version.core.interfaces.canvas import Canvas
from bosch_ASDIIE.Git_egylet.solid_version.core.interfaces.visualizable import Visualizable


class Visualizer:
    """
    This class handles the visualization of the objects of the game
    """
    def __init__(self, visualizable_objects: List[Visualizable], canvas: Canvas):
        self.visualizable_objects = visualizable_objects
        self.canvas = canvas

    def render(self):
        """
        This function is responsible for visualizing the visualizable objects
        :return:
        """
        self.canvas.clear()
        for obj in self.visualizable_objects:
            obj.draw(self.canvas)
        self.canvas.render()