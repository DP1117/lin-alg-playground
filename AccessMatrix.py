from tabulate import tabulate

# Return a row
@staticmethod
def get_row(matrix):
    print(tabulate(matrix))
    print("Enter the row number you want to return: ", end="")
    print("Here is the row:", matrix[int(input()) - 1])

# Return a column
@staticmethod
def get_column(matrix):
    print(tabulate(matrix))
    print("Enter the column number you want to return: ", end="")
    column_num = int(input()) - 1
    column = []
    for i in range(len(matrix)):
        column.append(matrix[i][column_num])
    print("Here is the column:", column)
