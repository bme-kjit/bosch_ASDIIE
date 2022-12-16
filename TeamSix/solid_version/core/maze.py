import random
import numpy as np
from TeamSix.solid_version.interfaces.steppable import Steppable
from TeamSix.solid_version.pacman.pacman import Pacman
from TeamSix.solid_version.interfaces.drawable import Drawable
from TeamSix.solid_version.enums.constans import Constants
from TeamSix.solid_version.maze_elements.wall import Wall
from TeamSix.solid_version.maze_elements.coin_holder import Coin_holder
from TeamSix.solid_version.maze_elements.coin import Coin
from TeamSix.solid_version.display.drawingService import DrawingService


class Maze(Drawable, Steppable):
    """
    Class for the maze
    """
    def __init__(self) -> None:
        self.fields = list(range(10))
        for f in range(0, len(self.fields)):
            self.fields[f] = list(range(10))

    def coin_removed(self):
        empty_fields = list(filter(lambda f: len(f.things == 0), np.array(self.fields).tolist()))
        rnd = random.randint(0, len(empty_fields))
        empty_fields[rnd].thing.append(empty_fields[rnd].position_x, empty_fields[rnd].position_y)
        return

    def init(self):
        """
        Creates a maze based a config size
        """
        # generate outer walls
        for x in range(0, Constants.MAZE_SIZE_X.value):
            self.fields[x][0] = Wall(x, 0)
            self.fields[x][Constants.MAZE_SIZE_Y.value - 1] = Wall(x, Constants.MAZE_SIZE_Y.value - 1)
        for y in range(0, Constants.MAZE_SIZE_Y.value):
            self.fields[0][y] = Wall(0, y)
            self.fields[Constants.MAZE_SIZE_X.value - 1][y] = Wall(Constants.MAZE_SIZE_X.value - 1, y)

        # other tiles are empty or walls
        for x in range(1, Constants.MAZE_SIZE_X.value - 1):
            for y in range(1, Constants.MAZE_SIZE_Y.value - 1):
                if (x is 1 and y is 1) or (x is 2 and y  is 1):
                    self.fields[x][y] = Coin_holder(x, y)
                # 10% chance of placing a wall, others are empty or have a coin with 30% chance
                chance_wall = random.randint(0, 9)
                if chance_wall == 0:
                    self.fields[x][y] = Wall(x, y)
                else:
                    coin_field = Coin_holder(x, y)
                    if random.randint(1, 9) == 1:
                        coin_field.things.append(Coin(coin_field))
                    self.fields[x][y] = coin_field

        self.set_neighbors()

    def set_neighbors(self):
        """
        Connects neighboring fields
        """
        for x in range(0, Constants.MAZE_SIZE_X.value):
            for y in range(0, Constants.MAZE_SIZE_Y.value):
                if x > 0:
                    self.fields[x][y].neighbors['LEFT'] = self.fields[x - 1][y]
                if y > 0:
                    self.fields[x][y].neighbors['UP'] = self.fields[x][y - 1]
                if x < Constants.MAZE_SIZE_X.value - 1:
                    self.fields[x][y].neighbors['RIGHT'] = self.fields[x + 1][y]
                if y < Constants.MAZE_SIZE_Y.value - 1:
                    self.fields[x][y].neighbors['DOWN'] = self.fields[x][y + 1]

    def place_pacman(self, field_x, field_y):
        """
        Palces pacman on given coordinates
        """
        # pacman starting field must be empty
        field = self.fields[field_x][field_y]
        field.things = []
        pacman = Pacman(field)
        field.things.append(pacman)
        return pacman

    def step(self):
        """
        Advances the elements in the maze one step
        """
        for x in self.fields:
            for y in x:
                y.step()

    def draw(self, service: DrawingService):
        """
        Draws the maze and its emelements
        """
        for i in self.fields:
            for j in i:
                j.draw(service)
