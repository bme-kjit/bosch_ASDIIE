from Objects.core.game_element import GameElement
from Objects.core.get_action import KeyEvent
from Objects.core.pacman_game_state import PacmanGameState
from Objects.core.pacman import Pacman


def test_WhenOneStep_IsTerminatedFalse():
    pacman_game_state = PacmanGameState([])
    pacman_game_state.step()
    assert not pacman_game_state.is_terminated(), \
        "The initialized game should not step into terminated state."


class GameElementIsCalledMock(GameElement):
    def __init__(self):
        self.is_take_action_called = False
        self.is_tick_called = False

    def take_action(self, key_event: KeyEvent):
        self.is_take_action_called = True

    def tick(self):
        self.is_tick_called = True


def test_whenTakeAction_thenGameElementsGetIt():
    game_element_mock = GameElementIsCalledMock()
    pacman_game_state = PacmanGameState([game_element_mock])
    pacman_game_state.take_action(KeyEvent.UP)
    assert game_element_mock.is_take_action_called, \
        "After the take_action called, the child GameElement objects" \
        " should get the key event."


def testPacmanGameState_whenStep_thenGameElementsTickCalled():
    game_element_mock = GameElementIsCalledMock()
    pacman_game_state = PacmanGameState([game_element_mock])
    pacman_game_state.step()
    assert game_element_mock.is_tick_called, \
        "After the step function called, tick function of " \
        "the child GameElement objects should be called."


def testPacmanGameState_whenPacmanMovesOneDirectionAfterInit_thenGameStateIsNotTerminated():
    pacman_game_state = PacmanGameState([Pacman()])
    for _ in range(5):
        pacman_game_state.step()
    assert not pacman_game_state.is_terminated(), \
        "When pacman moves in one direction and it is short, " \
        "then it does not die."
    for _ in range(50000):
        pacman_game_state.step()
    assert not pacman_game_state.is_terminated(), \
        "When pacman moves in one direction and it is short, " \
        "then it does not die."