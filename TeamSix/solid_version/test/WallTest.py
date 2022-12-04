from pacman import Pacman
from wall import Wall
from field import Field

def wall_kills_pacman():
    pacman = Pacman(Field(0,0))
    wall = Wall(1,0)
    
    wall.accept(pacman)

    assert pacman.dead is True