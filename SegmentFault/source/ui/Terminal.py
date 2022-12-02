"""
//*********************************************************************
//*********************************************************************
/ PROJECT_NAME : PacMan
/ FILENAME     : Terminal.py
/ AUTHOR       : Bozsóki Márk
/ UNIVERSITY   : BME
/ TEAM         : SegmentFault
**********************************************************************
**********************************************************************
/ Short description
/ --------------------------------------------------------------------
/ Module responsible for terminal input and output

/*********************************************************************
/*********************************************************************
"""

import os
from pathlib import Path

from source.ui.InputParser import InputParser
from source.map.MapDataReader import MapDataReader

class Terminal():
    def __init__(self):
        self.main_menuitems = [
            "start game",
            "game mode",
            "change map",
            "exit"
        ]

        self.gamemode_menuitems = [
            "standard", 
            "sandbox", 
            "back"
        ]

        self.changemap_menuitems = MapDataReader.list_mapdatas()
        self.changemap_menuitems.append("back")

        self.title = self.get_title()


    def show_menu(self, menutitle: str, menuitems: list[str]) -> None:
        """
        Displays the given menu

        @args:
            menutitle [str] - the title of the current menu
            menuitems [list(str)] - list containing the menuitems
        """
        self.clear()
        self.show_title()

        print(menutitle)
        index = 0
        for item in menuitems:
            #item = os.path.split(index)[1]
            #print(f"\t{index}. {item[:-7]}")
            print(f"  {index}. {item}")
            index += 1
        
        print("----------")


    def show_gameplayresult(self, time: int, score: int) -> None:
        """
        Displayes the gameplay results
        
        @args:

        """
        self.clear()
        self.show_title()

        print("GAME OVER")
        print(f"Game Time: {time}")
        print(f"Score: {score}")
        input("Press any key to continue...")


    def get_title(self):
        """
        Loads the title from local file
        """
        current_dir = os.path.dirname(__file__)
        parent_dir = Path(current_dir).parent.parent.absolute()
        title_source_path = os.path.join(parent_dir, "data/assets/TerminalTitle.txt")
        title_source = open(title_source_path, 'r')
        title = []

        while True:
            line = title_source.readline()

            # EndOfFile
            if not line:
                break

            if list(line)[-1]== '\n':
                title.append(list(line)[:-1])
            else:
                title.append(list(line))

        title_source.close()
        
        return title


    def show_title(self) -> None:
        """
        Displayes the gametitle
        """
        for line in self.title:
            for char in line:
                print(char, end='')
            print()


    def clear(self) -> None:
        """
        Clears the console
        """
        command = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)


    def get_menu_input(self, massage: str, *menuitems: list[str]) -> str:
        """
        Returns the parsed input from the user for menu contol

        @args:
            massage [str] - displayed massage for user
            menuitems [list(str)] - list containing the menuitems
        @return:
            parsed_input [str] - response from user
        """
        print(massage)
        raw_input =  input()
        parsed_input = InputParser.parse(raw_input, *menuitems)

        return parsed_input


    def get_gameplay_input(self, massage: str) -> str:
        """
        Returns the parsed input from the user for gameplay control

        @args:
            massage [str] - displayed massage for user
        @return:
            parsed_input [str] - response from user
        """
        print(massage)
        raw_input = input()
        parsed_input = InputParser.parse_single_input(raw_input)

        return parsed_input