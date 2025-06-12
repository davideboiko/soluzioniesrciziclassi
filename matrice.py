def sum_primary_diagonal(mat1: list[list[int], list[int], list[int]]):

    som1 = mat1[0][0] + mat1[1][1] + mat1[2][2]

    return f"Risultato prima diagonale 1.0: {som1}"

print(sum_primary_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

def sum_secondary_diagonal(mat1: list[list[int], list[int], list[int]]):

    som1 = mat1[2][2] + mat1[1][1] + mat1[0][0]

    return f"Risultato seconda diagonale  1.0: {som1}"

print(sum_secondary_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


def sum_primary_diagonal(mat1: list[list[int], list[int], list[int]]):

    som = 0
    for i in range(len(mat1)):

        som += mat1[i][i] 

    return f"Risultato prima diagonale 2.0: {som}"

print(sum_primary_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

def sum_secondary_diagonal(mat1: list[list[int], list[int], list[int]]):

    som = 0
    for i in range(len(mat1)):

        som += mat1[i][-i-1]

    return f"Risultato seconda diagonale 2.0: {som}"

print(sum_secondary_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
