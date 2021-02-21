import matplotlib.pyplot as plt
import random as rnd

x = [0]
y = [0]

for i in range(1, 50):
    x.append(x[i-1] + 1)
    y.append(rnd.random() * 100)

plt.plot(x, y)
plt.grid(True)
plt.title("Two dimention random walk")
plt.savefig("Random line plot.png")
plt.show()

