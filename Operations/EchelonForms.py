import copy
from tabulate import tabulate

# Row Echelon Form
def ref(matrix):
    copy_matrix = copy.deepcopy(matrix)
    print("Here is the ref from of your matrix:\n", tabulate(copy_matrix))
    return matrix

file = open("matrix.txt", "r")
data = file.readlines()
file.close()

matrix = []

for line in data:
  row = line.split(",")
  for i in range(len(row)):
    row[i] = float(row[i])
  matrix.append(row)

def print_matrix():
  for i in range(len(matrix)):
    row = "["
    for j in range(len(matrix[i])):
      row += str(matrix[i][j]) + ","
    print(row[:-1] + "]")

def interchange(r1, r2):
  matrix[r1], matrix[r2] = matrix[r2], matrix[r1]

def scale(r, s):
  for i in range(len(matrix[r])):
    matrix[r][i] *= s

def add(r1, r2, s):
  for i in range(len(matrix[r1])):
    matrix[r1][i] += matrix[r2][i] * s

def RREF():
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    pivot = 0
    for i in range(num_rows):
        if pivot >= num_cols:
            return
        temp = i
        while matrix[temp][pivot] == 0:
            temp += 1
            if temp == num_rows:
                temp = i
                pivot += 1
                if pivot == num_cols:
                  return
        interchange(temp, i)
        scale(i, 1 / matrix[i][pivot])
        for j in range(num_rows):
            if j != i:
                add(j, i, -matrix[j][pivot])
        pivot += 1
      
    
RREF()
print_matrix()


