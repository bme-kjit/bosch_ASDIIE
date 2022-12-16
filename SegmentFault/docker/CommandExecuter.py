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
from pathlib import Path

def GetCommads(source_file_path: str) -> list[str]:
    """
    Function reading the preaperd commands from file

    @args:
        sourceFile [str] - The path to the file containing the commannds
    @return:
        commands [list(str)] - The list of runnable commands
    """

    result = []

    # create file if not exists, and open for reading
    source_file = Path(source_file_path)
    source_file.touch(exist_ok=True)
    source = open(source_file, 'r')
    
    while True:
            line = source.readline()

            # EndOfFile
            if not line:
                break

            # delete '\n' charackter from end of line
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