import curses
from argparse import ArgumentParser

from bosch_ASDIIE.Git_egylet.solid_version.core.game import Game
from bosch_ASDIIE.Git_egylet.solid_version.core.move.key_listener import KeyListener
from bosch_ASDIIE.Git_egylet.solid_version.core.pacman_game_state import PacmanGameState
from bosch_ASDIIE.Git_egylet.solid_version.core.game_elements.pacman import Pacman
from bosch_ASDIIE.Git_egylet.solid_version.core.objects.pellets import Pellets
from bosch_ASDIIE.Git_egylet.solid_version.core.objects.walls import Walls
from bosch_ASDIIE.Git_egylet.solid_version.core.visualize.visualizer import Visualizer
from bosch_ASDIIE.Git_egylet.solid_version.gui.console_canvas import ConsoleCanvas
from bosch_ASDIIE.Git_egylet.solid_version.core.enum.map import MapSize
from bosch_ASDIIE.Git_egylet.solid_version.core.enum.screen import Screen
from bosch_ASDIIE.Git_egylet.solid_version.core.game_elements.score import Score
from bosch_ASDIIE.Git_egylet.solid_version.core.game_elements.terminate import Terminate

WIDTH = 10
HEIGHT = 10
PELLETS = 10
WALLS = 10
SCORE_PER_PELLET = 1


def main():
    arg_parser = ArgumentParser()
    arg_parser.add_argument("--gui", type=str, default="console")
    args = arg_parser.parse_args()

    screen = Screen()
    curses.cbreak()

    key_listener = KeyListener()
    key_listener.start(screen)

    pacman = Pacman(map_size=MapSize(HEIGHT, WIDTH))
    pellets = Pellets(map_size=MapSize(HEIGHT, WIDTH), number_pellets=PELLETS)
    walls = Walls(map_size=MapSize(HEIGHT, WIDTH), number_walls=WALLS)

    score = Score(score_per_pellet=SCORE_PER_PELLET, pacman=pacman, pellets=pellets)
    terminate = Terminate(pacman=pacman, walls=walls)

    visualizer = Visualizer([pacman, pellets, walls], ConsoleCanvas(MapSize(HEIGHT, WIDTH), screen))
    start_game_state = PacmanGameState([pacman, score, terminate])
    game = Game(key_listener, start_game_state, visualizer)
    game.run()

    # stop the screen
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()

    print(f"Game over, score:{score.get_score()}")


if __name__ == "__main__":
    main()