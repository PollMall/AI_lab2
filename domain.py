class Ruta:
    def __init__(self, pctA, pctB, dist):
        self.__pctA = pctA
        self.__pctB = pctB
        self.__dist = dist

    def getPctA(self):
        return self.__pctA

    def getPctB(self):
        return self.__pctB

    def getDist(self):
        return self.__dist

    def __str__(self):
        return str(self.__pctA) + " <-> " + str(self.__pctB) + " = " + str(self.__dist)

    def __gt__(self, other):
        if self.__dist > other.__dist:
            return True
        return False

    def __eq__(self, other):
        if self.__dist == other.__dist:
            return True
        return False
