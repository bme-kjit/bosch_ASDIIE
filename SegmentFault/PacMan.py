"""
*********************************************************************
*********************************************************************
PROJECT_NAME : PacMan
FILENAME     : PacMan.py
AUTHOR       : Juhász Pál Lóránd; Őri Gergely László; Seregi Bálint Leon; Bozsóki Márk
UNIVERSITY   : BME
TEAM         : SegmentFault
*********************************************************************
*********************************************************************
Short description
--------------------------------------------------------------------
Driver class and main script for our program

********************************************************************
********************************************************************
"""

import threading
import time
from source.TimerThread import TimeCounter
from source.Config import Config
from source.dynamic_elements.Direction import Direction
from source.dynamic_elements.movables.Player import Player
from source.map.MapData import MapData
from source.map.MapDataReader import MapDataReader
from source.map.MapGenerator import MapGenerator
from source.ui.Terminal import Terminal
from source.ui.Inputs import Inputs
from source.ui.GrayScaleVisualizer import GrayScaleVisualizer

class PacMan:
    def __init__(self):
        self.game_over = False
        self.user_input = Inputs.Nothing

        self.terminal = Terminal()
        self.config = Config()
        self.GAMEMODE, self.TIMEOUTLIMIT, self.MAP, self.GAMESPEED = self.config.Getsettings()
        self.timer = TimeCounter(self.TIMEOUTLIMIT)

        self.mapdata = MapData()

        self.show_menu()


    def show_menu(self):
        """ 
        """

        while self.user_input != "exit":

            self.game_over = False
            self.user_input = Inputs.Nothing
            self.terminal.show_menu("Main Menu", self.terminal.main_menuitems)
            self.user_input = self.terminal.get_menu_input("Choose menu option!", self.terminal.main_menuitems)

            # START GAME
            if self.user_input == "start game":
                self.start_game_session()
                self.user_input = Inputs.Nothing

            # GAMEMODE SETTINGS
            if self.user_input == "game mode":
                while self.user_input != "back":
                    self.terminal.show_menu("Change Gamemode", self.terminal.gamemode_menuitems)
                    self.user_input = self.terminal.get_menu_input("Choose gamemode option!", self.terminal.gamemode_menuitems)
                    
                    if self.user_input == "standard":
                        self.GAMEMODE = "standard"

                    if self.user_input == "sandbox":
                        self.GAMEMODE = "sandbox"

            # MAP SETTINGS
            if self.user_input == "change map":
                while self.user_input != "back":
                    self.terminal.show_menu("Maps", self.terminal.changemap_menuitems)
                    self.user_input = self.terminal.get_menu_input("Choose map option!", self.terminal.changemap_menuitems)
                    
                    if self.user_input == "Basic":
                        self.MAP = "Basic.mapdat"
                    
                    if self.user_input == "Bosch ASDIIE":
                        self.MAP = "Bosch ASDIIE.mapdat"

                    if self.user_input == "Clyde's Maze":
                        self.MAP = "Clyde's Maze.mapdat"

                    if self.user_input == "Double Trouble":
                        self.MAP = "Double Trouble.mapdat"

                    if self.user_input == "Horizontal":
                        self.MAP = "Horizontal.mapdat"

                    if self.user_input == "Vertical":
                        self.MAP = "Vertical.mapdat"

                    self.GAMEMODE = "standard"

                    #TODO: MAPDATA change based on the files contained in the "maps" directory
        
        self.terminal.clear()


    def start_game_session(self):
        """
        Configure session based on the settings and starts the game
        """

        # init mapdata
        if self.GAMEMODE == "standard":
            map_reader = MapDataReader()
            map_reader.load_mapdata(self.MAP)
            self.mapdata = map_reader.fill_mapdata()
        else:
            map_generator = MapGenerator()
            map_generator.generate_mapdata(map_width=25, map_height=25)
            self.mapdata = map_generator.fill_mapdata()
            
        # start game
        self.timer.StartStopperAdvanced()
        player_input_thread = threading.Thread(target=self.get_user_input)
        game_state = threading.Thread(target=self.calculate_game_state)

        player_input_thread.start()
        game_state.start()

        # gameover
        player_input_thread.join()
        game_state.join()


    def get_user_input(self):
        """
        Resives the user input during the game session
        """
        while not self.game_over or not self.timer.is_timeout:

            self.terminal.clear()
            self.terminal.show_title()

            self.user_input = Inputs.Nothing
            self.user_input = self.terminal.get_gameplay_input("Set new direction!")

            if self.user_input == Inputs.Exit:
                self.game_over = True
                break


    def calculate_game_state(self):
        """
        Implements the gameplay logic
        """

        # init Player (PacMan)
        player = Player(self.mapdata, self.mapdata.Player, Direction.Down)

        # prevent for instant gameover for sandbox mode
        if self.GAMEMODE == "sandbox":
            for safe_direction in Direction.__members__.values():
                if not player.is_wall_infront(self.mapdata, player.position, safe_direction):
                    player.direction = safe_direction
                    break

        #TODO: init Ghosts based on config

        #TODO: init enemies and collectables

        while not self.game_over or not self.timer.is_timeout:

            # player direction changing
            if self.user_input == Inputs.SetDirection_Up:
                player.next_direction = Direction.Up

            if self.user_input == Inputs.SetDirection_Right:
                player.next_direction = Direction.Right
            
            if self.user_input == Inputs.SetDirection_Down:
                player.next_direction = Direction.Down

            if self.user_input == Inputs.SetDirection_Left:
                player.next_direction = Direction.Left

            # refresh player position
            if self.GAMEMODE == "sandbox":
                # game over in sandbox mode if player hits the wall
                last_player_position = player.position
                player.position = player.get_next_position()
                if player.position == last_player_position:
                    # if the player not moved, than reached a wall -> game over
                    break
            else:
                player.position = player.get_next_position()

            # refresh mapdata info
            self.mapdata.Player = player.position

            # special command handling
            if self.user_input == Inputs.Restart:
                #TODO: implement game restart logic
                self.restart_game_session()
                break

            if self.user_input == Inputs.Exit:
                self.game_over = True
                break

            self.render_game_state()
            time.sleep(self.GAMESPEED)
        
        game_time = 2#self.timer.seconds_passed()
        self.terminal.show_gameplayresult(game_time, player.score)


    def restart_game_session(self):
        #TODO: implement session restart
        pass


    def render_game_state(self):
        """
        """
        visualiser = GrayScaleVisualizer(size_ratio=10)

        visualiser.refresh_game_state(self.mapdata)
        visualiser.render_game_state(self.mapdata.size)


# program entry point
if __name__ == "__main__":
    Game = PacMan()