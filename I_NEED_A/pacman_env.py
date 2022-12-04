#import the needed libraries
import cv2
import numpy as np

class PacMan:
    def __init__(self, map_size: int):
        '''
        This function is called by doing a constructor
        :param map_size:
        '''
        self.map_size = map_size
        self.body = None
        self.coins = []
        self.step_ = 100
        self.last_obs = None

        # Variables for visualizing the current grid world
        self.show_img_size = 300
        self.show_img = np.zeros((self.show_img_size, self.show_img_size, 3))
        self.ratio = int(self.show_img_size / self.map_size)
        self.score = 0
        self.reset()


    def step(self, action: int):
        '''
        This function is responsible for doing steps
        :param action: key control in range (0,3)
        :return: return parameters like an openai.gym environment
                state , reward , done , info
        '''

        # setting basic env status
        done_ = False
        
        # getting the current position
        pos_x, pos_y = self.body

        x , y = self.choose_action(pos_x=pos_x, pos_y=pos_y, action=action)

        #coordinates of the PacMan object
        self.body = (x,y)
        self._wall_limit()

        #Eat and add to score
        self.eat(x,y)

        # create observation
        obs = self._create_observation()

        # save observation
        self.last_obs = obs

        #decrement for termination , by reaching 0
        self.step_ -= 1

        #termination branch
        if self.step_ == 0:
            done_ = True


        #in this game not used
        info= None


        #end of episode
        return obs.flatten(), self.score, done_, info

    def choose_action(self, pos_x: int, pos_y: int, action: int):
        """
        The origin is top left[0,0]
        :param pos_x: the horizontal position of our agent
        :param pos_y: the vertical position of the agent
        :param action: movement variable , 0-->down , 1-->right , 2-->up , 3-->left
        :return:  both axis position
        """
        if action == 0:
            # going down
            x, y = self.right(pos_x, pos_y)
        elif action == 1:
            # going right
            x, y = self.up(pos_x, pos_y)

        elif action == 2:
            # going up
            x, y = self.left(pos_x, pos_y)

        elif action == 3:
            # going left
            x, y = self.down(pos_x, pos_y)

        else:
            #in case of wrong key
            if action != 0 or action != 1 or action != 2 or action != 3:
                raise TypeError("Only integers between 0 and 3 are accepted")
            done_ = True
            self.score= -1
            print(f"Score {self.score}")

        return x , y

    def eat(self, x: int, y: int):
        '''
        Remove coins
        :param x: pac-man's x coordinate
        :param y: pac-man's y coordinate
        :return: None
        '''
        if (x, y) in self.coins:
            # increment score by eating an object
            self.score += 1

            # if object reached  , remove
            self.coins.remove((x, y))

    def right(self, x: int, y: int):

        #only the horizontal coordinate changes

        x += 1
        return x,y


    def up(self, x: int, y: int):

        #only the vertical coordinate changes
        y += 1
        return x,y

    def left(self, x: int, y: int):

        # only the horizontal coordinate changes
        x -= 1
        return x,y


    def down(self, x: int, y: int):

        #only the vertical coordinate changes
        y -= 1
        return x,y


    def reset(self) -> np.ndarray:
        """
        This function resets the valuables to the initial state
        :param:
        :return (np.ndarray): Observation
        """
        # reset environment parameters
        self.body = None
        self.coins = []
        self.step_ = 0
        self.last_obs = None

        # create pac-man, foods and the observation
        self._create_body()
        self._create_coins(num=10)
        obs_ = self._create_observation()
    
        return obs_.flatten()


    def render(self):
        """
        Creates a cv2 plot from the current game state.
        :param:
        :return: None
        """
        if self.last_obs is not None:
            img = np.float32(self.last_obs)
        else:
            img = np.float32(self._create_observation())
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        # rescale original image from the grid world to visualize with OpenCv
        for i in range(self.show_img_size):
            for j in range(self.show_img_size):
                self.show_img[i][j] = img[i // self.ratio][j // self.ratio]
        cv2.imshow("PAC-MAN Env", self.show_img)
        # add wait to see the game
        cv2.waitKey(50)


    def _create_coins(self, num: int):
        """"
        Generate coins (foods for pac-man).
        :param num (int): number of coins (foods) to create
        :return: None
        """
        while _<range(num):
            coordinates = tuple(np.random.randint(0, self.map_size, (2,)))
            if self.body[0] != coordinates[0] and self.body[1] != coordinates[1]:
                self.coins.append(coordinates)


    def _create_body(self):
        """"
        Gives initial position for pac-man.
        :param:
        :return: None
        """
        self.body = (0,0)


    def _create_observation(self) -> np.ndarray:
        """
        Creates a grayscale observation (image) from the current state of the game.
        :param:
        :return obs_ (np.ndarray): Observation
        """
        # init map
        obs_ = np.zeros((self.map_size, self.map_size, 1))

        # add coins
        for obj in self.coins:
            obs_[obj[0], obj[1], 0] = 0.25

        # add pac-man
        pac_man_coordinates = self.body
        obs_[pac_man_coordinates[0], pac_man_coordinates[1], 0] = 0.8
        return obs_


    def _wall_limit(self):
        """
        Limit pac-man to step outside the map.
        :param:
        :return: None
        """
        limited_x = max(0, min(self.body[0], self.map_size-1))
        limited_y = max(0, min(self.body[1], self.map_size-1))
        
        self.body = (limited_x,limited_y)





if __name__ == "__main__":

    map_size = 20
    EPISODES = 3
    done_ = False

    # calling Constructor for the game
    env = PacMan(map_size=map_size)

    # starting state
    state = env.reset()

    # render before first step
    env.render()

    # play loop
    while not done_:
        # here are declared the control keys
        print("0->down  1->right    2->up   3->left")

        # add the next action
        action = int(input("Next action:\n"))

        # gym compatible return of step
        state, reward, done_, info = env.step(action=action)

        # visualization of the game
        env.render()

        # stop the game
        if done_:
            break

    print(f" Game over, your score is : {env.score}")
    env.reset()