from Repository import *

if __name__ == '__main__':
    repository=DomainRepository("input.txt")
    repository.readFromFile()
    for line in repository.getMatrix():
        for col in line:
            print(col)
        print()