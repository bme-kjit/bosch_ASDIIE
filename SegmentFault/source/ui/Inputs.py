"""
//*********************************************************************
/ PROJECT_NAME : PacMan
/ FILENAME     : Inputs.py
/ AUTHOR       : Bozsóki Márk
/ UNIVERSITY   : BME
/ TEAM         : SegmentFault
**********************************************************************
**********************************************************************
/ Short description
/ --------------------------------------------------------------------
/ Collection of input command definitions

/*********************************************************************
/*********************************************************************
"""

from enum import Enum

class Inputs(str, Enum):

    SetDirection_Up = 'w'
    SetDirection_Right = 'd'
    SetDirection_Down = 's'
    SetDirection_Left = 'a'
    Restart = "r"
    Exit = "q"
    Nothing = ""
