from typing import List
from core.interface.canvas import Canvas
from core.interface.visualizable import Visualizable


class Visualizer:
    def __init__(self,
                 visualizable_objects: List[Visualizable],
                 canvas: Canvas):
        """
        Constructor of the Visualizer which responsible for visualizing
        :param visualizable_objects: The list of objects to display
        :param canvas: The canvas class that encapsulates the drawing functions
        """
        self.visualizable_objects = visualizable_objects
        self.canvas = canvas

    def render(self) -> None:
        """
        Calls the draw function of each object which is wished to be displayed and draw it on the canvas
        :return: None
        """
        self.canvas.clear()
        for obj in self.visualizable_objects:
            obj.draw(self.canvas)
        self.canvas.render()
