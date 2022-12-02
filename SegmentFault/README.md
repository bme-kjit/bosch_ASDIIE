<h1 align="center">SegmentFault's Pac-Man <img src="https://www.cs.toronto.edu/~ylzhang/csc309w16/t6/pacman.gif" width="3%"></h1>

## :scroll: Description

This repository is for student work at the class of **Agile Software Development in Industrial Environment**. The course is at *Budapest University of Technology and Economics* and is hosted by *Robert Bosch Kft*.

This project is develped by a group of four students, as an assignment for the class.


```
git clone https://github.com/markbozsoki/bosch_ASDIIE.git
```

## :mortar_board: About the game

Pac-Man is an action maze chase video game.

The player controls the eponymous character through an enclosed maze. The objective of the game is to eat all of the dots placed in the maze while avoiding four colored ghosts — Blinky (red), Pinky (pink), Inky (cyan), and Clyde (orange) — that pursue Pac-Man. When Pac-Man eats all of the dots, the player advances to the next level.

<p align="center"><img src="https://acegif.com/wp-content/uploads/2022/fzk5d/30-huge-maze-pacman.gif"></p>

<h4 align="right">Learn more about Pac-Man at - https://en.wikipedia.org/wiki/Pac-Man</h4>

## :joystick: How to play

**The actions and commands are case-*in*sensitive!**

| Action | Key | Alias |
| :---: | :---: | :---: |
| Up | W | 5 |
| Right | D | 3 |
| Down | S | 2 |
| Left | A | 1 |

---

| Commands | Key | Aliases |
| :---: | :---: | :--- |
| restart | r | new, reset |
| exit | q | end, quit |

<details><summary>Hint!</summary><br>
Every words listed in the Commands table are valid command. Except "Commands", "Key" and "Aliases"... :wink:
</details>

## :rocket: Development

<details><summary><h3> Phase 1 </h3></summary>

- [x] Empty map without walls
- [x] Can move left, right, up, down
- [x] Step after some seconds
- [x] Collect points
- [x] Game terminates after a given timesteps

</details>

<details><summary><h3> Phase 2 </h3></summary>

- [x] Implement wall features on the sides
- [x] Extend to in-map walls (walls inside the map)
- [x] Game Over feature (hits wall = die)
- [ ] Implement 3 unit tests

</details>

## :toolbox: Testing

**Use the unittest command line interface to run tests**

To run all unit tests named "test_ModuleName.py":
```
$ cd ../SegmentFault/test
$ python3 -m unittest discover
```


To run single unit test modules or cases:
```
$ cd ../SegmentFault/test
$ python3 -m unittest <parent_directory>.<testmodule_name>.<testcase_name>
```

## :muscle: Collaborators
  
  - [**Amontobix**](https://github.com/Amontobix)
  - [**leonsuszter**](https://github.com/leonsuszter)
  - [**origergelylaszlo**](https://github.com/origergelylaszlo)

<p align="right"><sub>2022</sub></p>
