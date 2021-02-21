import os, sys
import matplotlib.pyplot as plt

args = sys.argv

if 'C:\\' in args[-1]:
    fqfile = args[-1]
    for i in range(-1, -len(args[-1]), -1):
        if args[-1][i] == '\\':
            fqname = args[-1][i+1:]
            break
else:
    fqfile = os.getcwd() + '\\' + sys.argv[-1]
    fqname = sys.argv[-1]

with open(fqfile, 'r') as fqsample:
    i = 0
    lens = []
    for line in fqsample:
        i += 1
        if i == 2:
            lens.append(len(line))
            i = 0

plt.plot(lens)
plt.grid(True)
plt.title("Distribution of length of sequences in \n" + fqname)
plt.xlabel("Number of sequence")
plt.ylabel("Length of sequence")
plt.show()
