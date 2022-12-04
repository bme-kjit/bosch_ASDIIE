import numpy as np
import os

# Enumerating the participants of the PacMan game
EMPTY = 0
PACMAN = 1
DOT = 2


class PacMan:
    def __init__(self, map_size: int = 10, max_time_step: int = 100, num_of_dots: int = 10):
        """
        PacMan Game
        :param map_size: dimension of the map [size x size] (int)
        :param max_time_step: after how many steps should the game be ended (int)
        :param num_of_dots: number of randomly generated edible dots (int)
        """
        # PacMan variables
        self.map_size = map_size
        self.time_step_cnt = 0
        self.max_time_step = max_time_step
        self.dots = []
        self.num_of_dots = num_of_dots
        self.pacman = [0, 0]
        self.score = 0

    def reset(self) -> np.ndarray:
        """
        Resets the environment
        :return: Current state of the map (np.ndarray)
        """
        # Reset variables
        self.time_step_cnt = 0
        self.dots = []
        self.score = 0

        # Generating the initial position of Pacman
        self.pacman[0] = np.random.randint(0, self.map_size)
        self.pacman[1] = np.random.randint(0, self.map_size)

        # Generating random edible dots
        self.generate_dots()

        # Creating observation
        observation = self.create_observation()

        return observation

    def step(self, action: str) -> [np.ndarray, int, bool]:
        """
        Steps the environment into its next state
        :param action: current user input (w, a ,s or d) (str)
        :return: current state of the map (np.ndarray), current score (int), terminating flag (bool)
        """
        terminate = False

        # Increasing the timestep
        self.time_step_cnt += 1

        # Moving pacman based on current action
        self.move_pacman(action)

        # Check whether Pacman picked up an edible dot
        self.check_dots()

        # Creating observation
        observation = self.create_observation()

        # Terminating after max time steps
        if self.time_step_cnt > self.max_time_step:
            terminate = True

        return observation, self.score, terminate

    def render(self, observation: np.ndarray, action: str = 'w') -> None:
        """
        Prints the current state of the environment on the console
        :param action: Current user input (str)
        :param observation: Current state of the map (np.ndarray)
        :return: -
        """
        # Clearing console before printing the map (cannot clear the console in PyCharm, only in terminal)
        os.system('cls' if os.name == 'nt' else 'clear')
        # Converting numpy array to python list
        observation = observation.tolist()

        # Replacing number with characters for visualization
        for x in range(self.map_size):
            for y in range(self.map_size):
                if observation[x][y] == EMPTY:
                    observation[x][y] = '-'
                elif observation[x][y] == PACMAN:
                    observation[x][y] = '0'
                elif observation[x][y] == DOT:
                    observation[x][y] = '+'

        # Printing the current score and the current observation line by line with separation
        for line in observation:
            print(*line, sep='  ')

        print("\nCurrent score:", self.score)

        print("Invalid input! Please use w, a, s or d!") if action not in ['w', 'a', 's', 'd'] else None

    def create_observation(self) -> np.ndarray:
        """
        Processes the positions of Pacman and the edible dots and creates the current state matrix
        :return: Current state of the map (np.ndarray)
        """
        # Creating the map
        observation = np.zeros((self.map_size, self.map_size), dtype=int)

        # Placing Pacman on the map
        observation[self.pacman[0], self.pacman[1]] = PACMAN

        # Placing the edible dots on the map
        for dot in self.dots:
            observation[dot[0], dot[1]] = DOT

        return observation

    def move_pacman(self, action: str) -> None:
        """
        Moves Pacman in the desired direction
        :param action: current user input (w, a, s or d) (str)
        :return: -
        """
        # Moving up
        if action == 'w':
            self.pacman[0] = max(self.pacman[0] - 1, 0)
        # Moving left
        elif action == 'a':
            self.pacman[1] = max(self.pacman[1] - 1, 0)
        # Moving down
        elif action == 's':
            self.pacman[0] = min(self.pacman[0] + 1, self.map_size - 1)
        # Moving right
        elif action == 'd':
            self.pacman[1] = min(self.pacman[1] + 1, self.map_size - 1)

    def generate_dots(self) -> None:
        """
        Generates the given number of random edible dots on the map
        :return: -
        """
        for _ in range(self.num_of_dots):
            dot_coords = tuple(np.random.randint(0, self.map_size, (2,)))

            # Making sure that the generated dots do not have the same position with each other or with Pacman
            while (dot_coords in self.dots) or (dot_coords == tuple(self.pacman)):
                dot_coords = tuple(np.random.randint(0, self.map_size, (2,)))

            self.dots.append(dot_coords)

    def check_dots(self) -> None:
        """
        Checks whether Pacman picked up a dot and increases the score accordingly
        :return: -
        """
        for dot in self.dots:
            if dot == tuple(self.pacman):
                # If Pacman moved on a dot, increase the score and remove the dot
                self.score += 1
                self.dots.remove(dot)


if __name__ == "__main__":
    # Instantiating the environment
    env = PacMan(map_size=10,
                 max_time_step=100,
                 num_of_dots=10)

    # Reset environment and render the initial state
    state = env.reset()
    env.render(state)

    done = False

    while not done:
        user_input = input("Select your next action (w, a, s, d): ")
        state, reward, done = env.step(user_input)
        env.render(state, user_input)
