import curses


class Screen:
    """
    This class is for visualizing the game in the Terminal
    """
    def __init__(self):
        self.screen = curses.initscr()

    def __getattr__(self, attr):
        return getattr(self.screen, attr)