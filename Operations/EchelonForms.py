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
  for i in range(min(len(matrix), len(matrix[0]))):
    # interchange row to have a non-zero entry in the ith column
    for k in range(i, len(matrix)):
      if matrix[k][i] != 0:
        interchange(i, k)
        break
    # scale the ith row by 1/matrix[i][i]
    s = matrix[i][i]
    if s == 0:
      continue  
    scale(i, 1/matrix[i][i])
    # reduce all ith column entries to 0
    for k in range(len(matrix)):
      if k == i:
        continue
      add(k, i, -matrix[k][i])
      
    
RREF()
print_matrix()


