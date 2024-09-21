import copy
from tabulate import tabulate

# Adds two rows
@staticmethod
def add_rows(matrix):
    copy_matrix = copy.deepcopy(matrix)
    print(tabulate(copy_matrix))
    print("Enter the two rows you want to add (r1, r2): ", end = "")
    row_nums = input().split(",")
    r1, r2 = int(row_nums[0]) - 1, int(row_nums[1]) - 1
    rows = [copy.deepcopy(copy_matrix[r1]), copy.deepcopy(copy_matrix[r2])]
    print("Do you want to scale the row/rows before adding? (y/n) ", end = "")
    if input() == "y":
        print("Enter the row/rows you want to scale (r1,r2,both): ", end = "")
        row_num = input()
        if str(row_num) == "both" or int(row_num) - 1 == r1:
            rows[0] = scale_row(r1, copy_matrix[r1])
        if str(row_num) == "both" or int(row_num) - 1 == r2:
            rows[1] = scale_row(r2, copy_matrix[r2])
    print("Enter the row you want to add onto (r1, r2): ", end = "")
    r = int(input()) - 1
    row_num = 0 if r == r1 else 1 
    other_num = 1 if row_num == r1 else 0
    for i in range(len(copy_matrix[0])):
        rows[row_num][i] += rows[other_num][i]
    copy_matrix[r] = rows[row_num]
    print("Here is your edited matrix:\n", tabulate(copy_matrix))
    return copy_matrix
        

# Scales a row
@staticmethod
def scale_rows(matrix):
    print()
    copy_matrix = copy.deepcopy(matrix)

# Interchanges a row
@staticmethod
def interchange_rows(matrix):
    print()
    copy_matrix = copy.deepcopy(matrix)

def scale_row(row_num, row):
    copy_row = copy.deepcopy(row)
    print(f"Enter the scalar you want to multiply by for row {str(row_num + 1)}: ", end = "")
    scalar = int(input())
    for i in range(len(copy_row)):
        copy_row[i] *= scalar
    return copy_row