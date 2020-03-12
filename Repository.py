from Domain import *


class DomainRepository:
    def __init__(self, fileName):
        self.__nrOfCities = 0
        self.__matrix = []
        self.__fileName = fileName

    def getNrOfCities(self):
        return self.__nrOfCities

    def getMatrix(self):
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
            for line in file:
                numbers = line.split(",")
                pctB = 0
                for nr in numbers:
                    self.save(Ruta(pctA, pctB, int(nr)))
                    pctB += 1
                pctA += 1
