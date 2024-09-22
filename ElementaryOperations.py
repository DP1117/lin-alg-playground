import copy
from tabulate import tabulate

# Adds two rows
@staticmethod
def add_rows(matrix):
    copy_matrix = copy.deepcopy(matrix)
    print(tabulate(copy_matrix))
    print("Enter the two rows you want to add (x1, x2): ", end = "")
    row_nums = input().split(",")
    x1, x2 = int(row_nums[0]) - 1, int(row_nums[1]) - 1
    rows = [copy.deepcopy(copy_matrix[x1]), copy.deepcopy(copy_matrix[x2])]
    print("Do you want to scale the row/rows before adding? (y/n) ", end = "")
    if input() == "y":
        print("Enter the row/rows you want to scale (x1, x2, both): ", end = "")
        row_num = input()
        if str(row_num) == "both" or int(row_num) - 1 == x1:
            rows[0] = scale_row(x1, copy_matrix[x1])
        if str(row_num) == "both" or int(row_num) - 1 == x2:
            rows[1] = scale_row(x2, copy_matrix[x2])
    print("Enter the row you want to add onto (x1, x2): ", end = "")
    r = int(input()) - 1
    row_num = 0 if r == x1 else 1 
    other_num = 1 if row_num == x1 else 0
    for i in range(len(copy_matrix[0])):
        rows[row_num][i] += rows[other_num][i]
    copy_matrix[r] = rows[row_num]
    print("Here is your edited matrix:\n", tabulate(copy_matrix))
    return copy_matrix
        

# Scales a row
@staticmethod
def scale_rows(matrix):
    copy_matrix = copy.deepcopy(matrix)
    print(tabulate(copy_matrix))
    print("Enter the row you want to scale (x): ", end = "")
    row_num = int(input()) - 1
    copy_matrix[row_num] = scale_row(row_num, copy_matrix[row_num])
    print("Here is your edited matrix:\n", tabulate(copy_matrix))
    return copy_matrix

# Interchanges a row
@staticmethod
def interchange_rows(matrix):
    copy_matrix = copy.deepcopy(matrix)
    print(tabulate(copy_matrix))
    print("Enter the two rows you want to interchange (x1, x2): ", end = "")
    row_nums = input().split(",")
    x1, x2 = int(row_nums[0]) - 1, int(row_nums[1]) - 1
    temp = copy_matrix[x1]
    copy_matrix[x1] = copy_matrix[x2]
    copy_matrix[x2] = temp
    print("Here is your edited matrix:\n", tabulate(copy_matrix))
    return copy_matrix

def scale_row(row_num, row):
    copy_row = copy.deepcopy(row)
    print(f"Enter the scalar you want to multiply by for row {str(row_num + 1)}: ", end = "")
    scalar = int(input())
    for i in range(len(copy_row)):
        copy_row[i] *= scalar
    return copy_row