import curses


class Screen:
    """
    A class for encapsulating the screen ( = curses.initscr()) object, thus helping
    with readability
    """
    def __init__(self):
        self.screen = curses.initscr()

    def __getattr__(self, attr):
        return getattr(self.screen, attr)