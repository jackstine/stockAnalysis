import os

PREVIOUS_DIRECTORY = None

def getFromDict(json, key):
    if (key in json.keys()):
        return json[key]
    else:
        return None

def changeDir(fileName):
    """
    :param fileName: == __file__   for all uses
    changes the directory to the file location
    """
    global PREVIOUS_DIRECTORY
    PREVIOUS_DIRECTORY = os.curdir
    abspath = os.path.abspath(fileName)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

def switchBackDir():
    global PREVIOUS_DIRECTORY
    if (PREVIOUS_DIRECTORY != None):
        os.chdir(PREVIOUS_DIRECTORY)