def show_file(nume_fis):
    with open(nume_fis, 'r') as file:
        for x in file:
            print(x)


def create_matrix(nume_fis):
    matrix = []
    with open(nume_fis, 'r') as file:
        file.readline()
        for line in file:
            matrix.append([])
            numbers = line.split(",")
            for nr in numbers:
                matrix[-1].append(int(nr.split("\n")[0]))
    return matrix


def det_drum_minim_greedy(matrix):
    parcurse = [1]
    while len(parcurse) != len(matrix):
        min = max(matrix[parcurse[-1] - 1])

        for j in range(len(matrix[parcurse[-1] - 1])):
            if (matrix[parcurse[-1] - 1][j] < min) and ((j + 1) not in parcurse) and (matrix[parcurse[-1]-1][j]!=0):
                min = matrix[parcurse[-1] - 1][j]
                min_index = j + 1
        parcurse.append(min_index)
    # parcurse.append(max(parcurse)+1)
    return parcurse
def cost_drum_minim(parcurse):
    sum=0
    for i in range(len(parcurse)-1):
        sum+=matrix[parcurse[i]-1][parcurse[i+1]-1]
    return sum

if __name__ == '__main__':
    nume_fis = "input.txt"
    # show_file(nume_fis)
    matrix = create_matrix(nume_fis)
    parcurse=det_drum_minim_greedy(matrix)
    print(len(matrix))
    print(parcurse)
    print(cost_drum_minim(parcurse))