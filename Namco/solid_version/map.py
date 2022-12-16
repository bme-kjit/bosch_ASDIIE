import numpy as np
from constants import MapEnum


class Map:
    def __init__(self, map_enum=MapEnum, map_size: int = 10):
        """
        :param map_enum: constants for map tiles (enum)
        :param map_size: size of the map (int)
        Map class: Initializing the map with restricted areas and award slots
        """
        # Markers for different objects
        self.agent_slot = map_enum.AGENT_SLOT.value
        self.restricted_slot = map_enum.RESTRICTED_SLOT.value
        self.award_slot = map_enum.AWARD_SLOT.value
        self.terminating_slot = map_enum.TERMINATING_SLOT.value
        self.empty_slot = map_enum.EMPTY_SLOT.value

        # Generating the map
        self.map_size = map_size
        self.map = np.ndarray(shape=(self.map_size, self.map_size), dtype='<U1')
        self._generate_map()

    def _create_map_borders(self):
        """
        Defines the borders of the map as restricted area
        :return: -
        """
        self.map[0, :] = self.restricted_slot
        self.map[-1, :] = self.restricted_slot
        self.map[:, 0] = self.restricted_slot
        self.map[:, -1] = self.restricted_slot

    def _create_restricted_areas(self):
        """
        Creating restricted areas on the map
        :return: -
        """
        # Restricted areas should not be near the top or bottom wall to avoid unreachable areas
        for row in range(2, self.map_size - 2):
            # Restricted area cannot start near vertical map borders to avoid unreachable areas
            area_start = np.random.randint(2, self.map_size - 2)
            area_length = np.random.randint(self.map_size - 1 - area_start)
            # Placing restricted area on the map
            self.map[row, area_start:(area_start + area_length)] = self.restricted_slot

    def _create_award_slots(self):
        """
        Filling the empty areas with award slots
        :return: -
        """
        self.map[self.map != self.restricted_slot] = self.award_slot

    def _generate_map(self):
        """
        Places every object on the map
        :return:
        """
        self._create_map_borders()
        self._create_restricted_areas()
        self._create_award_slots()

    def update_map(self, agent_pos: [int, int], done: bool) -> np.ndarray:
        """
        Updates the map based on the agent's position
        :param agent_pos: x and y coordinate of the agent (int, int)
        :param done: Game over flag (bool)
        :return: Updated map (np.ndarray)
        """
        x = agent_pos[0]
        y = agent_pos[1]

        # Agent's previous position must be emptied
        self.map[self.map == self.agent_slot] = self.empty_slot

        # The agent should be placed into its current position
        self.map[x][y] = self.agent_slot

        # Marking place of agent's death on map
        if done:
            self.map[self.map == self.agent_slot] = self.terminating_slot

        return self.map

    def check_interaction(self, agent_pos: [int, int]) -> [bool, bool]:
        """
        Checks whether the agent interacted with any objects on the map
        :return: Restricted slot flag (bool), award slot flag (bool)
        """
        award_interaction = False
        restricted_interaction = False

        x = agent_pos[0]
        y = agent_pos[1]

        # Checking whether the agent interacted with an award slot
        if self.map[x][y] == self.award_slot:
            award_interaction = True
        # Checking whether the agent interacted with a restricted slot
        elif self.map[x][y] == self.restricted_slot:
            restricted_interaction = True

        return award_interaction, restricted_interaction
