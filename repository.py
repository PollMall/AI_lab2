from domain import *


class RutaRepository:
    def __init__(self, fileName):
        self.__src=-1
        self.__dest=-1
        self.__nrOfCities = 0
        self.__matrix = []
        self.__fileName = fileName
        self.readFromFile()

    def getNrOfCities(self):
        return self.__nrOfCities

    def getSrc(self):
        return self.__src

    def getDest(self):
        return self.__dest

    def getFileName(self):
        return self.__fileName

    def findAll(self):
        return self.__matrix

    def findOne(self, ruta):
        return self.__matrix[ruta.getPctA()][ruta.getPctB()]

    def save(self, ruta):
        if len(self.__matrix) == 0 or len(self.__matrix[-1]) == self.__nrOfCities:
            self.__matrix.append([])
        self.__matrix[-1].append(ruta)

    def readFromFile(self):
        with open(self.__fileName, "r") as file:
            self.__nrOfCities = int(file.readline())
            pctA = 0
            for i in range(self.__nrOfCities):
                line=file.readline()
                numbers = line.split(",")
                pctB = 0
                for nr in numbers:
                    self.save(Ruta(pctA, pctB, int(nr)))
                    pctB += 1
                pctA += 1
            self.__src=int(file.readline())-1
            self.__dest=int(file.readline())-1