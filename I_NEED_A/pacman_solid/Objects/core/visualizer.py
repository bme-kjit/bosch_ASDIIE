from typing import List
from Objects.core.canvas import Canvas
from Objects.core.visualizable import Visualizable


class Visualizer:
    def __init__(self,
                 visualizable_objects: List[Visualizable],
                 canvas: Canvas):
        self.visualizable_objects = visualizable_objects
        self.canvas = canvas

    def render(self):
        self.canvas.clear()
        for obj in self.visualizable_objects:
            obj.draw(self.canvas)
        self.canvas.render()