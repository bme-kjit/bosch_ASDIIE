import unittest
from bosch_ASDIIE_Namco.Namco.solid_version.pac_man import PacMan
from bosch_ASDIIE_Namco.Namco.solid_version.constants import ActionEnum


class MyTestCase(unittest.TestCase):
    # Unit test for the process_action method
    def test_whenTheInputIsString_PacmansPositionChanges(self):
        x, y = 0, 0
        agent = PacMan(ActionEnum, x, y)
        agent.process_action('w')
        agent.x, agent.y = agent.position
        self.assertListEqual([x - 1, y], [agent.x, agent.y])

        agent.process_action('a')
        agent.x, agent.y = agent.position
        self.assertListEqual([x - 1, y - 1], [agent.x, agent.y])

        agent.process_action('s')
        agent.x, agent.y = agent.position
        self.assertListEqual([x, y - 1], [agent.x, agent.y])

        agent.process_action('d')
        agent.x, agent.y = agent.position
        self.assertListEqual([x, y], [agent.x, agent.y])
        "When the user input is one of the required inputs," \
        "then Pacman's position changes correctly"

    def test_whenTheInputIsNotString_NothingChanges(self):
        x, y = 0, 0
        agent = PacMan(ActionEnum, x, y)
        agent.process_action(True)
        agent.x, agent.y = agent.position
        self.assertListEqual([x, y], [agent.y, agent.y])

        agent = PacMan(ActionEnum, x, y)
        agent.process_action(1)
        agent.x, agent.y = agent.position
        self.assertListEqual([x, y], [agent.y, agent.y])
        "When the user input is not one of the required inputs," \
        "then Pacman's position doesn't change"


if __name__ == '__main__':
    unittest.main()
