import threading

from core.key_interaction.key_event import KeyEvent


class KeyListener:

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
                if key in KeyEvent._value2member_map_:
                    self.last_key = key
            except:
                pass

    def stop(self) -> None:
        """

        :return: None
        """
        self.stopped = True
        self.thread.join()

        self.screen.timeout(-1)
        self.screen = None

    def start(self, screen) -> None:
        """

        :param screen:
        :return: None
        """
        self.screen = screen
        self.thread = threading.Thread(target=self.listen, daemon=True)
        self.stopped = False
        self.thread.start()

    def has_happened(self) -> bool:
        """

        :return:
        """
        return self.last_key is not None

    def read_last_key_event(self) -> KeyEvent:
        """

        :return:
        """
        if self.last_key is None:
            raise ValueError("KeyBoardListener has not noticed "
                             "any key event that could be read.")

        if self.last_key == KeyEvent.UP.value:
            key_event = KeyEvent.UP
        elif self.last_key == KeyEvent.RIGHT.value:
            key_event = KeyEvent.RIGHT
        elif self.last_key == KeyEvent.DOWN.value:
            key_event = KeyEvent.DOWN
        elif self.last_key == KeyEvent.LEFT.value:
            key_event = KeyEvent.LEFT
        self.last_key = None

        return key_event
