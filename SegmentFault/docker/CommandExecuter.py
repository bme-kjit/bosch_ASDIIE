"""
*********************************************************************
*********************************************************************
PROJECT_NAME : PacMan
FILENAME     : CommandExecuter.py
AUTHOR       : Bozsóki Márk
UNIVERSITY   : BME
TEAM         : SegmentFault
*********************************************************************
*********************************************************************
Short description
--------------------------------------------------------------------
Script responsible for reading predefined commands from file
and running them

********************************************************************
********************************************************************
"""

import os

def GetCommads(sourceFile: str) -> list[str]:
    """
    Function reading the preaperd commands from file

    @args:
        sourceFile [str] - The path to the file containing the commannds
    @return:
        commands [list(str)] - The list of runnable commands
    """
    source = open(sourceFile, 'r')
    result = []
    while True:
            line = source.readline()

            # EndOfFile
            if not line:
                break

            if line[-1] == '\n':
                result.append(line[:-1])
            else:
                result.append(line)

    source.close()
    return result


def RunCommands(commands: list[str]) -> None:
    """
    Function running the required CLI commands

    @args:
        commands [list(str)] - The list of runnable commands
    """

    for cmd in commands:
        print(cmd)
        os.system(str(cmd))


if __name__ == "__main__":
    commands = GetCommads("commands.txt")
    RunCommands(commands)