import curses

from Objects.core.game import Game
from Objects.core.step import  KeyboardListener
from Objects.core.map import MapSize
from Objects.core.screen import Screen
from Objects.core.visualizer import Visualizer

from Objects.core.pacman_game_state import PacmanGameState
from Objects.core.pacman import Pacman
from Objects.gui.console_canvas import ConsoleCanvas


WIDTH = 5
HEIGHT = 5



def main():

    # using curses lib for proper keyboard-canvas interaction through SSH
    screen = Screen()
    curses.cbreak()

    key_listener = KeyboardListener()
    key_listener.start(screen)

    pacman = Pacman(map_size=MapSize(HEIGHT, WIDTH))
    visualizer = Visualizer([pacman], ConsoleCanvas(MapSize(HEIGHT, WIDTH), screen))
    start_game_state = PacmanGameState([pacman])
    game = Game(key_listener, start_game_state, visualizer)
    game.run()

    # stop the screen
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()
    print("Game Over :(")

if __name__ == "__main__":
    main()