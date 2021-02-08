import random as rnd
import matplotlib.pyplot as plt

x = [0]
y = [0]

for i in range(1,100):
    x.append(x[i-1] + rnd.sample([0,1,-1], k = 1)[0])
    if x[i] == x[i - 1]:
        y.append(y[i-1] + rnd.sample([1,-1], k = 1)[0])
    if x[i] != x[i - 1]:
        y.append(y[i-1] + 0)

plt.plot(x,y)

plt.show()
