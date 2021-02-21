import matplotlib.pyplot as plt
import seaborn as sns
import random as rnd


x = [0]
y = [0]

for i in range(1, 50):
    x.append(rnd.random() * 100)
    y.append(rnd.random() * 100)

z = [x,y]

#plt.violinplot(z)
sns.catplot(x = z[0], y = z[1], data = z, kind="violin")
plt.grid()
plt.title("Violin plot")
plt.show()
