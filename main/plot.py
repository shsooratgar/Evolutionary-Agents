import matplotlib.pyplot as plt
import numpy as np

mins = []
means = []
maxes = []

with open('results.txt', 'r') as f:
    content = f.readlines()
    content = [x.strip() for x in content]

for line in content:
    line = line.split()
    mins.append(float(line[0]))
    means.append(float(line[1]))
    maxes.append(float(line[2]))

x_axis = list(range(len(mins)))
plt.plot(x_axis, mins)
plt.plot(x_axis, means)
plt.plot(x_axis, maxes)

plt.show()
