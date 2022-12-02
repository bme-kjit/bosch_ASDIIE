import random
from Pybranch.core.collide import Collide
from Pybranch.core.list import ListToBool
from Pybranch.core.dot_creation import DotCreation
from Pybranch.core.dot_creator import DotCreator
from Pybranch.core.inner_wall import InnerWall
from Pybranch.core.border_wall import BorderWall
from Pybranch.core.create_wall import CreateWall
from Pybranch.core.screen_elements import Colors
import pygame

dots_number = random.randint(10, 70)
every_sprite = pygame.sprite.Group()
walls = pygame.sprite.Group()
dots = pygame.sprite.Group()


def test_wall():
    inner_wall = InnerWall(CreateWall(Colors()))
    border = BorderWall(CreateWall(Colors()))
    inner_wall.create_wall(walls, every_sprite)
    border.create_wall(walls, every_sprite)
    walls_list = pygame.sprite.Group.sprites(walls)
    number_of_walls = len(inner_wall.pos_list) + len(border.pos_list)
    assert len(walls_list) == number_of_walls


def test_number_of_dots():
    dot_creation = DotCreation(DotCreator(Collide(), ListToBool()))
    dot_creation.creation.dot_creator(dots_number, walls, dots, every_sprite)
    dots_list = pygame.sprite.Group.sprites(dots)
    assert len(dots_list) == dots_number


def test_collision():
    collision = pygame.sprite.groupcollide(walls, dots, False, False)
    collision_list = collision.values()
    assert len(collision_list) == 0


