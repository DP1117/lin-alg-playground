import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import inv as invert

# returns [[a], [b]] where ax + b = y
def regression_line(x_data, y_data):
    if len(x_data) != len(y_data):
        return 0
    M = []
    v = []
    for i in range(len(x_data)):
        M.append([x_data[i], 1])
        v.append([y_data[i]])
    M_trans = np.matrix_transpose(M)
    return np.matmul(np.matmul(invert(np.matmul(M_trans, M)), M_trans), v)

def calc_error(actual_x, actual_y, a, b):
    expected_y = a * actual_x + b
    return pow(actual_y - expected_y, 2)

def total_error(x_data, y_data, a, b):
    sum_error = 0
    for i in range(len(x_data)):
        x_point = x_data[i]
        y_point = y_data[i]
        sum_error += calc_error(x_point, y_point, a, b)
    return sum_error

fig, ax = plt.subplots()

x_lim = [-50, 50]
y_lim = [-50, 50]

ax.set_xlim(x_lim[0], x_lim[1])
ax.set_ylim(y_lim[0], y_lim[1])

x_data = []
y_data = []

f = open("2D_data.txt")
data = f.readlines()
f.close()

for i in range(len(data)):
    datapoint = data[i].split(',')
    x_data.append(float(datapoint[0]))
    y_data.append(float(datapoint[1]))

fitted_line = regression_line(x_data, y_data)
a = fitted_line[0][0]
b = fitted_line[1][0]

print(total_error(x_data, y_data, a, b))

plt.plot(x_data, y_data, 'ro')
plt.plot([(y_lim[0] - b)/a,(y_lim[1] - b)/a], y_lim,'b')
plt.text(5, 45, "y = " + str(round(a, 3)) + "x" + " + " + str(round(b, 3)))

plt.savefig('2D_Data_output.png')
plt.show()