import threading

from bosch_ASDIIE.Git_egylet.solid_version.core.enum.key_event import KeyEvent


class KeyListener:
    """
    This class handles the keyboard events in remote environments in a side-thread
    """
    KEYPRESS_TO_KEY_EVENT = {
        "KEY_UP": KeyEvent.UP,
        "KEY_DOWN": KeyEvent.DOWN,
        "KEY_LEFT": KeyEvent.LEFT,
        "KEY_RIGHT": KeyEvent.RIGHT,
    }
    MILLISECONDS = 1000

    def __init__(self):
        self.screen = None
        self.last_key = None
        self.thread = None
        self.stopped = False

    def listen(self):
        self.screen.keypad(True)
        self.screen.timeout(self.MILLISECONDS)

        while not self.stopped:
            try:
                key = self.screen.getkey()
                if key in self.KEYPRESS_TO_KEY_EVENT:
                    self.last_key = key
            except:
                pass

    def stop(self):
        self.stopped = True
        self.thread.join()

        self.screen.timeout(-1)
        self.screen = None

    def start(self, screen):
        self.screen = screen
        self.thread = threading.Thread(target=self.listen, daemon=True)
        self.stopped = False
        self.thread.start()

    def has_happened(self):
        return self.last_key is not None

    def read_last_key_event(self) -> KeyEvent:
        if self.last_key is None:
            raise ValueError("KeyBoardListener has not noticed "
                             "any key event that could be read.")
        key_event = self.KEYPRESS_TO_KEY_EVENT[self.last_key]
        self.last_key = None
        return key_event