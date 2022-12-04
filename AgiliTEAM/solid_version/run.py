import curses

from core.game import Game
from core.key_interaction.key_listener import KeyListener
from core.pacman_game_state import PacmanGameState
from core.game_element.pacman import Pacman
from core.game_element.pellets import Pellets
from core.game_element.ghosts import Ghosts
from core.game_element.walls import Walls
from core.display.visualizer import Visualizer
from gui.console_canvas import ConsoleCanvas
from core.misc.map import MapSize
from core.misc.config_loader import ConfigLoader
from core.display.screen import Screen
from core.game_element.score_counter import ScoreCounter
from core.game_element.defeat_checker import DefeatChecker
from core.misc.custom_argument_parser import CustomArgParser


def main():

    config_loader = ConfigLoader('default_config.yaml')
    default_config = config_loader.load_config()

    arg_parser = CustomArgParser(default_config)
    parsed_config = arg_parser.get_parsed_config()

    screen = Screen()
    curses.cbreak()

    key_listener = KeyListener()
    key_listener.start(screen)

    map_size = MapSize(parsed_config.map_height, parsed_config.map_width)

    walls = Walls(map_size=map_size, internal_walls=parsed_config.internal_walls)
    pacman = Pacman(map_size=map_size, known_pos=[walls.pos])
    pellets = Pellets(map_size=map_size, num_pellets=parsed_config.num_pellets, known_pos=[pacman.pos, walls.pos])
    ghosts = Ghosts(map_size=map_size, num_ghosts=parsed_config.num_ghosts, walls_pos=walls.pos,
                    known_pos=[pacman.pos, pellets.pos, walls.pos], step_confidence=parsed_config.step_confidence)
    score_counter = ScoreCounter(base_score=parsed_config.base_score, difficulty=parsed_config.difficulty,
                                 pacman=pacman, pellets=pellets)
    defeat_checker = DefeatChecker(pacman=pacman, ghosts=ghosts)

    canvas = ConsoleCanvas(map_size, screen)

    visualizer = Visualizer([walls, ghosts, pellets, pacman], canvas)
    start_game_state = PacmanGameState([pacman, pellets, ghosts, walls, score_counter, defeat_checker])

    game = Game(key_listener, start_game_state, visualizer, parsed_config.difficulty)
    game.run()

    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()


if __name__ == "__main__":
    main()
