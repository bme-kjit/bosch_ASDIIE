"""
//*********************************************************************
//*********************************************************************
/ PROJECT_NAME : PacMan
/ FILENAME     : metrics.py
/ AUTHOR       : Pal Lorand Juhasz
/ UNIVERSITY   : BME
/ TEAM         : SegmentFault
**********************************************************************
**********************************************************************
/ Short description
/ --------------------------------------------------------------------
/
Script that creates metric analysis from the code base source files

/*********************************************************************
/*********************************************************************
"""
import os
import subprocess
from os import walk
from pathlib import Path


header0 = "*******************************************\n"
header1 = "***               METRICS               ***\n"
header3 = "***                                     ***\n"
header4 = "********************************************\n"
header = header0 + header3 + header1 + header3 + header0 + "\n\n"


separator0 = "<-----------Cyclomatic Complexity----------->\n\n\n"
separator1 = "\n\n\n<-----------Maintainability Index----------->\n\n\n"

#Choose main working dir
PATH = ""
#Choose metrics file path
textfilepath = "docker\\metrics.txt"

Path0 = "\\source\\dynamic_elements\\emergers"
Path1 = "\\source\\dynamic_elements\\movables"
Path2 = "\\source\\map"
Path3 = "\\source\\ui"
Path4 = "\\source"

def WalkDirTree(dir_path):
    # list to store files name

    resultFiles = []
    resultDirs = []
    fullpaths = []
    for (dir_path, dir_names, file_names) in walk(dir_path):
        resultFiles.extend(file_names)
        resultDirs.extend(dir_names)
        # fullpath = f"{dir_path}{dir_names}{file_names}"
        # fullpaths.append(fullpath)
    return resultFiles, resultDirs, fullpaths


def SortList(list):
    listsroted = []
    for element in list:
        if Path(element).suffix == '.py' and (element != "__init__.py") and (not "test" in element):
            listsroted.append(element)
    return listsroted


def GetRadonData(pyfilespath, type):
    Filestr = ""
    FilestrCC = ""
    for files in pyfilespath:
        cmd = f"radon {type} {files} -s"
        temp = subprocess.Popen(cmd, stdout = subprocess.PIPE)
        output = str(temp.communicate())
        Chunkedoutput = output[3:-12]
        if type == "cc":
            GoodOutPut = ""
            mylist = Chunkedoutput.split(" ")
            mylist[0] = mylist[0][:-4]
            GoodOutPut = GoodOutPut + " ".join(mylist)
            FilestrCC = FilestrCC + GoodOutPut + "\n"
        Filestr = Filestr + Chunkedoutput + "\n"
    if type == "mi":
        return Filestr
    if type == "cc":
        return FilestrCC

def GetRadonDataSimple(type, path):
    Filestr = ""
    FilestrCC = ""
    cmd = f"radon {type} {path}"
    temp = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    output = str(temp.communicate())
    Chunkedoutput = output[3:-12]
    if type == "cc":
        GoodOutPut = ""
        mylist = Chunkedoutput.split(" ")
        mylist[0] = mylist[0][:-4]
        GoodOutPut = GoodOutPut + " ".join(mylist)
        FilestrCC = FilestrCC + GoodOutPut + "\n"
    Filestr = Filestr + Chunkedoutput + "\n"
    if type == "mi":
        return Filestr
    if type == "cc":
        return FilestrCC

def GetRadonDataComplex(MainDir,Subdirs, type):
    Dir = f"{MainDir}{Subdirs}"
    pyfilespathorg = os.listdir(Dir)
    pyfilespath = SortList(pyfilespathorg)
    print(pyfilespath)
    Filestr = ""
    FilestrCC = ""
    for files in pyfilespath:
        os.chdir(Dir)
        cmd = f"radon {type} {files} -s"
        temp = subprocess.Popen(cmd, stdout = subprocess.PIPE)
        output = str(temp.communicate())
        Chunkedoutput = output[3:-12]
        if type == "cc":
            GoodOutPut = ""
            mylist = Chunkedoutput.split(" ")
            mylist[0] = mylist[0][:-4]
            GoodOutPut = GoodOutPut + " ".join(mylist)
            FilestrCC = FilestrCC + GoodOutPut + "\n"
        Filestr = Filestr + Chunkedoutput + "\n"
    if type == "mi":
        return Filestr
    if type == "cc":
        return FilestrCC


FilestrCC0 = GetRadonDataComplex(PATH, Path0,"cc")
FilestrMI0 = GetRadonDataComplex(PATH, Path0 ,"mi")

FilestrCC1 = GetRadonDataComplex(PATH, Path1,"cc")
FilestrMI1 = GetRadonDataComplex(PATH, Path1 ,"mi")

FilestrCC2 = GetRadonDataComplex(PATH,Path2,"cc")
FilestrMI2 = GetRadonDataComplex(PATH,Path2 ,"mi")

FilestrCC3 = GetRadonDataComplex(PATH, Path3, "cc")
FilestrMI3 = GetRadonDataComplex(PATH, Path3, "mi")

FilestrCC4 = GetRadonDataComplex(PATH, "", "cc")
FilestrMI4 = GetRadonDataComplex(PATH, "", "mi")
#print(Filestr)


FilestrCC5 = GetRadonDataComplex(PATH,Path4,"cc")
FilestrMI5 = GetRadonDataComplex(PATH,Path4 ,"mi")

FilestrCC = FilestrCC0 + FilestrCC1 + FilestrCC2 + FilestrCC3 + FilestrCC5 + FilestrCC4
FilestrMI = FilestrMI0 + FilestrMI1 + FilestrMI2 + FilestrMI3 + FilestrMI5 + FilestrMI4
#newstrCC = FormatStrN(FilestrCC)


Filestr = f"{header}{separator0}{FilestrCC}{separator1}{FilestrMI}"
filepointer = open(textfilepath, "w")

filepointer.write(Filestr)
filepointer.close()
