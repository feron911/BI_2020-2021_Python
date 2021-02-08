import os, sys, random

args = sys.argv

if 'C:\\' in args[-1]:
    txtfile = args[-1]
else:
    txtfile = os.getcwd() + '\\' + sys.argv[-1]

with open(txtfile, "r") as txtin, open(txtfile + "_random", "w") as txtout:
    li_of_rev = []
    for line in txtin:
        li_of_word = line.split()
        for word in li_of_word:
            if len(word) > 3:
                i = list(word[1:len(word) - 1])
                random.shuffle(i)
                word = word[0] + "".join(i) + word[len(word) - 1]
            li_of_rev.append(word)
        txtout.write(' '.join(li_of_rev) + '\n')
        li_of_rev = []