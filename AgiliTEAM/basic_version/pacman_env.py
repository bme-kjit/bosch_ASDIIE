from typing import Tuple, Union
import cv2
import numpy as np
np.random.seed(0)

ACTION_SPACE_SIZE = 4
DIRECTIONS = {"up": 0, "right": 1, "down": 2, "left": 3}


class Pacman:
    """
    ------------------------
    Pacman Environment Class
    ------------------------


    Attributes:
        map_size : int
            size of the square map's one side
        action_space : ndarray
            defines the executable actions in the environment
        coins_pos : list (of tuples)
            contains the (x, y) coordinate pairs of the generated coin objects
        ghosts_pos : list (of tuples)
            contains the (x, y) coordinate pairs of the generated ghost objects
        pos : tuple
            defines the position of PacMan
        step_counter : int
            keeps track of the executed steps throughout the game
        score : int
            keeps track of the points acquired throughout the game
        orientation : int
            defines PacMan's facing direction
        state : ndarray
            defines an array representing the game status
        image_size : int = 600
            passed as an argument to the constructor, defines the size of the displayed visualization window
        image : ndarray
            BGR channel image array, which is displayed in the render function
        ratio : int
            image_size divided by the MAP_SIZE, used for the visualization window in image preprocessing
        num_coins : int = 100
            number of coins generated on the map
        num_ghosts : int = 4
            number of ghosts generated on the map
        score_coin : int = 10
            value of each collected coin
        max_step : int = 100
            termination limit value


    Methods:
        __init__(self, image_size: int = 600, map_size: int = 30, max_step: int = 100, num_ghosts: int = 4,
                 num_coins: int = 100, score_coin: int = 10) -> None
        reset(self) -> numpy.ndarray
        step(self, action: int) -> Tuple[numpy.ndarray, float, bool, str]
        render(self) -> None
        _create_image(self) -> None
        _move(self) -> None
        _get_info(self) -> str
        _get_reward(self, state: numpy.ndarray) -> float
        _get_next_state(self, action: int) -> numpy.ndarray
        _set_action(self, action: int | None) -> None
        _check_action_validity(self, action: int) -> bool
        _calculate_score(self) -> None
        _check_done(self) -> bool
        _generate_pos(self, object_name: str, num_objects: int) -> None
        _update_map(self) -> numpy.ndarray
    """
    def __init__(self, image_size: int = 600, map_size: int = 30, max_step: int = 100, num_ghosts: int = 4,
                 num_coins: int = 100, score_coin: int = 10) -> None:
        """
        Constructs the basic components of the Pacman Environment Class.
        :return: None
        """
        self.map_size = map_size
        self.action_space = np.arange(ACTION_SPACE_SIZE)
        self.state = None

        self.num_coins = num_coins
        self.num_ghosts = num_ghosts
        self.coins_pos = []
        self.ghosts_pos = []
        self.score_coin = score_coin
        self.pos = None

        self.max_step = max_step
        self.step_counter = None
        self.score = None
        self.orientation = None

        self.image_size = image_size
        self.image = np.zeros((self.image_size, self.image_size, 3))
        self.ratio = int(self.image_size / self.map_size)

        self.reset()

    def reset(self) -> np.ndarray:
        """
        This function resets the game session and returns a newly generated game state.
        :return: current state of the game (empty map with PacMan, ghosts and coins generated)
        """
        self.step_counter = 0
        self.score = 0
        self.orientation = np.random.randint(ACTION_SPACE_SIZE)

        self.ghosts_pos = []
        self.coins_pos = []

        self._generate_pos('self_pos', 1)
        self._generate_pos('ghost', self.num_ghosts)
        self._generate_pos('coin', self.num_coins)

        self.state = self._update_map()

        return self.state

    def step(self, action: int) -> Tuple[np.ndarray, float, bool, str]:
        """
        This function formulates the (next_state, reward, done, info) values, thus moving the game one step forward.
        :param action: chosen action 0/1/2/3 corresponding to the directions in order up/right/down/left)
        :return:
            next_state : ndarray
                state of the environment after the action
            reward : float
                quantification of the state transition ###(To be implemented...)###
            done : bool
                True if the game is terminated, otherwise False
            info : str
                contains information about the game progress (scores acquired, steps)
        """
        next_state = self._get_next_state(action)
        reward = self._get_reward(next_state)
        done = self._check_done()
        info = self._get_info()

        return next_state, reward, done, info

    def render(self) -> None:
        """
        This function creates a visualization of the game state.
        :return: None
        """
        self._create_image()
        cv2.imshow("AgiliTEAM Pacman Environment", self.image)
        cv2.waitKey(50)

    def _create_image(self) -> None:
        """
        This function processes the environment's state and creates the image array according to the given display size.
        :return: None
        """
        for i in range(self.image_size):
            for j in range(self.image_size):
                self.image[i][j] = self.state[i // self.ratio][j // self.ratio]

    def _get_info(self) -> str:
        """
        This function creates an 'info' string which can be used as a feedback from the environment itself.
        :return: information about the game's current state
        """
        self._calculate_score()
        info = "Points acquired: " + str(self.score) + "\nSteps: " + str(self.step_counter) + "/" + str(self.max_step)

        return info

    def _get_reward(self, state: np.ndarray) -> float:
        """
        This function realizes the reward function and formulates the value based on the state passed as an argument.
        :param state: ndarray of the game state based on which the reward value is calculated
        :return: reward value from which the agent is able to learn
        """
        # Only for RL purposes
        # TODO: add implementation of reward function
        reward = 0.0

        return reward

    def _get_next_state(self, action: int) -> np.ndarray:
        """
        This function realizes the change in the game state according to the chosen action.
        :param action: chosen action 0/1/2/3 corresponding to the directions in order up/right/down/left)
        :return: state of the environment after the action
        """
        valid = self._check_action_validity(action)
        if valid:
            self._set_action(action)
        self._move()
        self.state = self._update_map()

        return self.state

    def _move(self) -> None:
        """
        This function modifies PacMan's position according to its facing direction.
        :return: None
        """
        # if facing of the game_state_test == _direction_:
        #     if game_state_test is at the end of the map:
        #         move to the opposite side
        #     else:
        #         move a unit in the _direction_
        if self.orientation == DIRECTIONS["up"]:
            self.pos[0] = self.map_size - 1 if self.pos[0] - 1 < 0 else self.pos[0] - 1
        elif self.orientation == DIRECTIONS["right"]:
            self.pos[1] = 0 if self.pos[1] + 1 == self.map_size else self.pos[1] + 1
        elif self.orientation == DIRECTIONS["down"]:
            self.pos[0] = 0 if self.pos[0] + 1 == self.map_size else self.pos[0] + 1
        elif self.orientation == DIRECTIONS["left"]:
            self.pos[1] = self.map_size - 1 if self.pos[1] - 1 < 0 else self.pos[1] - 1

        self.step_counter += 1

    def _set_action(self, action: Union[int, None]) -> None:
        """
        This function coordinates the modification of the 'orientation' variable based on user and timer (To be
        implemented...) input.
        :param action: chosen action 0/1/2/3 corresponding to the directions in order up/right/down/left)
        :return: None
        """
        self.orientation = action
        # Timer response to be implemented later...

    def _check_action_validity(self, action: int) -> bool:
        """
        This function verifies the user input's validity.
        :param action: chosen action 0/1/2/3 corresponding to the directions in order up/right/down/left)
        :return: True if the user input action is valid
        """
        if min(self.action_space) <= action <= max(self.action_space):
            return True
        else:
            raise ValueError("Please enter a number in the [0; {0}) interval!".format(ACTION_SPACE_SIZE))

    def _calculate_score(self) -> None:
        """
        This function calculates the scores which may have been acquired during the last step, and if so, removes the
        coin from the map.
        Score calculation:
            +10 / coin collected
        :return: None
        """
        for coin_pos in self.coins_pos:
            if self.pos == coin_pos:
                self.score += self.score_coin
                self.coins_pos.remove(coin_pos)

    def _check_done(self) -> bool:
        """
        This function analyzes the game state and decides whether it's terminated or not.
        :return: True if the game is terminated, otherwise False
        """
        if self.step_counter > self.max_step:
            print("Time step limit reached!")
            return True

        for ghost_pos in self.ghosts_pos:
            if self.pos == ghost_pos:
                print("You have been caught by a ghost!")
                return True

        return False

    def _generate_pos(self, object_name: str, num_objects: int) -> None:
        """
        This function generates (x, y) coordinate pairs randomly in the available spots.
        :param object_name: name of the object to be generated across the map
        :param num_objects: number of objects for coordinates
        :return: None
        """
        for _ in range(num_objects):
            pos = list(np.random.randint(self.map_size, size=(2,)))
            while pos in self.coins_pos or pos == self.pos or pos in self.ghosts_pos:
                pos = list(np.random.randint(self.map_size, size=(2,)))

            if object_name == 'ghost':
                self.ghosts_pos.append(pos)
            elif object_name == 'coin':
                self.coins_pos.append(pos)
            elif object_name == 'self_pos':
                self.pos = pos
            else:
                raise NotImplementedError("Not implemented for the given object name!")

    def _update_map(self) -> np.ndarray:
        """
        This function updates the game state according to the modified coordinates in position tuples.
        :return: game state after modification
        """
        state = np.zeros((self.map_size, self.map_size))

        for coin_pos in self.coins_pos:
            state[coin_pos[0], coin_pos[1]] = 0.25

        for ghost_pos in self.ghosts_pos:
            state[ghost_pos[0], ghost_pos[1]] = 0.5

        state[self.pos[0], self.pos[1]] = 1

        return state
