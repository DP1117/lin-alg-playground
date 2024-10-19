import copy 
from tabulate import tabulate

# Creates matrix
@staticmethod
def create_matrix():
    print("Enter the size of the 2D-matrix (m,n): ", end="")
    dim = input().split(",")
    m, n = int(dim[0]), int(dim[1])
    matrix = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            print(tabulate(matrix))
            print(f"Enter the ({i+1},{j+1}) entry: ", end="")
            matrix[i][j] = int(input())
    print("Here is your matrix:\n", tabulate(matrix))
    return matrix

# Changes an entry in an matrix
@staticmethod
def change_entry(matrix):
    copy_matrix = copy.deepcopy(matrix)
    print(tabulate(copy_matrix))
    print("Enter the entry you want to change (x,y): ", end="")
    entry_pos = input().split(",")
    print("Enter the new value: ", end="")
    new_val = int(input())
    copy_matrix[int(entry_pos[0]) - 1][int(entry_pos[1]) - 1] = new_val
    print("Here is your edited matrix:\n", tabulate(copy_matrix))
    return copy_matrix
    