import inspect, os

class Process:
    fileFolder = "/managefiles/"

    def __init__(self, name):
        self.name = name
        self.fileName = "Threading" + self.name + ".txt"
        self.thread = None
        self.stop = False
        self.directory = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        self.filePath = self.directory + self.fileFolder + self.fileName

    def run(self):
        while(not self.stop):
            self.spawnNewTxt()
            self.command()
            self.responseToUser()
            self.timeSync()
        self.onStop()

    def spawnNewTxt(self):
        f = open(self.filePath, 'w')
        f.close()

    def responseToUser(self): 
        f = open(self.filePath, 'r')
        fileStuff = f.read()
        if (len(fileStuff) > 0):
            if (fileStuff[0] == 'Y'):
                self.stop = True

    def command(self):
        if (self.startTime()):
            process = self.createprocess()
            process.run()

    def createProcess(self):
        pass

    def onStop(self):
        pass

    def timeSync(self):
        pass

    def startTime(self):
        pass
