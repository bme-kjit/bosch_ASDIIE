from pacman_env import Pacman

if __name__ == "__main__":

    env = Pacman()
    done = False
    state = env.reset()
    while not done:
        env.render()
        action = int(input("Choose your action:\n0 - move up\n1 - move right\n2 - move down\n3 - move left\n"
                           "Your choice: "))
        next_state, reward, done, info = env.step(action=action)
        print(info)
        state = next_state
    print("End of game")
