"""
//*********************************************************************
//*********************************************************************
/ PROJECT_NAME : PacMan
/ FILENAME     : Config.py
/ AUTHOR       : Pal Lorand Juhasz
/ UNIVERSITY   : BME
/ TEAM         : SegmentFault
**********************************************************************
**********************************************************************
/ Short description
/ --------------------------------------------------------------------
/
Creates and handles arguments

optional arguments:
  -h, --help            show this help message and exit
  --gamemode GAMEMODE, -gm GAMEMODE
                        Determins game type, standard/sandbox
  --timeout TIMEOUT, -to TIMEOUT, --int TIMEOUT
                        Determins the time in seconds after the game ends. By default it is 180 s
  --map MAPDATA, -m MAPDATA, --str MAPDATA
                        The path of the mapdata container file, but generated can be used
  --gamespeed GAMESPEED, -gs GAMESPEED
                        Value of the gamespeed in step rate can be 1,2,3. If user gives invalid value
                        gamespeed will be 1.

/*********************************************************************
/*********************************************************************
"""

import argparse


class Config():

    def __init__(self) -> None:
        self.Arguments = argparse.ArgumentParser(prog = "SegmentFault's Pacman")
        self.AddArguments()
        self.GivenArguments = self.Arguments.parse_args()


    def AddArguments(self) -> None:
        """
        Initializes the flag with the help of argparse module

        @args:
            self
        @return:
                None
        """

        self.Arguments.add_argument("--gamemode", "-gm",
                                    action='store',
                                    help="Determins game type, standard/sandbox ", 
                                    default="sandbox")
        self.Arguments.add_argument("--timeout", "-to", '--int',
                                    help="Determins the time in seconds after the game ends. By default it is 180 s",
                                    default="180")
        self.Arguments.add_argument("--map", "-m", '--str',
                                    help="The path of the mapdata container file, but generated can be used",
                                    default="Basic.mapdat")
        self.Arguments.add_argument("--gamespeed", "-gs", 
                                    help="Value of the gamespeed in step rate can be 1,2,3. If user gives invalid "
                                         "value gamespeed will be 1",
                                    default=1)



    def GetGamemode(self) -> str:
        """
        Returns the value of the given gamemode flag
        
        @args:
            self

        @return:
                gamemode [str]
        """
        gamemode = self.GivenArguments.gamemode
        return gamemode


    def GetTimeout(self) -> int:
        """
        Returns the value of the given timeout flag
        
         @args:
             self

         @return:
                 Timeout[int]
         """

        Timeoutlimit = self.GivenArguments.timeout
        return int(Timeoutlimit)


    def GetMapdata(self) -> str:
        """
        Returns the value of the given mapdata flag
        
        @args:
            self

        @return:
            Mapdatafile[str]
        """

        Mapdatafile = self.GivenArguments.map
        return Mapdatafile


    def GetGamespeed(self) -> float:
        """
        Returns the value of the given GameSpeed flag
        
        @args:
            self

        @return:
                GameSpeed[float]
        """

        Gamespeed = self.ScaleUpGamespeed()
        return Gamespeed


    def Getsettings(self) -> tuple:
        """
        Returns the value of the flags given to the program upon starting it
        
        @args:
            self

        @return:
                tuple - containing: gamemode, Timeout, Mapdatafile, GameSpeed
        """

        gamemode = self.GetGamemode()
        Timeout = self.GetTimeout()
        Mapdatafile = self.GetMapdata()
        GameSpeed = self.GetGamespeed()
        return gamemode, Timeout, Mapdatafile, GameSpeed

    def CheckGamespeed(self) -> int:
        """ 
        Checks if the given gamespeed flag has the correct value,
        if it is not corrects it
        
        @args:
            self

        @return:
                GameSpeed[int]
        """

        GameSpeed = int(self.GivenArguments.gamespeed)
        if (GameSpeed > 3) or (GameSpeed <= 0):
            GameSpeed = 1
        return GameSpeed

    def ScaleUpGamespeed(self, rate = 1.5) -> float:
        """ 
        Returns the scaled gamespeed
        
        @args:
            self
            rate[float]: rate of conversion
        @return:
                GameSpeed
        """

        GameSpeed = float(self.CheckGamespeed())
        if GameSpeed == 1.0:
            return GameSpeed
        else: return GameSpeed * rate