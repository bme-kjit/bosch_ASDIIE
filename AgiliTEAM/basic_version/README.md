# AgiliTEAM's PacMan
```
authors:
Vitay Vanda      - XLUA51  
Nyeste Pál       - M9G6U6
Pelenczei Bálint - C4QFEY
```
This repository is for student work at the class of Agile Software Development in Industrial Environment.

The course is at Budapest University of Technology and Economics and is hosted by Robert Bosch Kft.

## Project summary
The initial task was to implement a Pac-Man game in small groups, based on clean code principles, that can be further
developed throughout the course.

## Instructions
Issue the following commands to gather all the required files and libraries:
```bash
git clone https://github.com/BPelenczei/AgiliTEAM
cd AgiliTEAM/AgiliTEAM/
pip3 install -e .
```
To start the game, run the `pacman.py` file via the `python3 pacman.py` command.

For the PacMan control keys, see the table below:

| Action | Key |
|:------:| :---: |
|   Up   | 0 |
| Right  | 1 | 1 |
|  Down  | 2 |
|  Left  | 3 |

## About the game
**Pac-Man** is an action maze chase video game; the player controls the eponymous character through an enclosed maze.

The **objective** of the game is to eat all of the dots placed in the maze while avoiding four colored ghosts — Blinky
(red), Pinky (pink), Inky (cyan), and Clyde (orange) — that pursue Pac-Man. When Pac-Man eats all of the dots, the
player advances to the next level. If Pac-Man is caught by a ghost, he will lose a life; the game ends when all lives
are lost.

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/en/5/59/Pac-man.png" />
</p>

<p align="right">
  For more information, check out the game's Wikipedia: https://en.wikipedia.org/wiki/Pac-Man
</p>

## Functions

### First stage:
- Readme for the pacman
- Empty map without walls
- Can move left, right, up, down
- Collects points
- Game terminates after a given timestep

## Files
- `pacman.py` - core game file
- `pacman_env.py` - environment definition file
- `README.md`