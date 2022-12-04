import curses


class Screen:
    def __init__(self):
        self.screen = curses.initscr()

    def __getattr__(self, attr):
        return getattr(self.screen, attr)
