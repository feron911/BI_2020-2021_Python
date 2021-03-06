import pandas as pd
import matplotlib.pyplot as plt

train = pd.read_csv("https://raw.githubusercontent.com/Serfentum/bf_course/master/14.pandas/train.csv")
train.to_csv("train.csv")
train = train.fillna(0)

train_bar = train[["pos", "A", "G", "T", "C"]]

train_bar.plot(x = "pos", stacked = True, mark_right = True, kind = 'bar', figsize = (20,10),
               fontsize = 8, xlabel = "Position", title = "Nucleotide read content per position",
               ylabel = "Proportion of every nucleotides")


train_part = train[train["matches"] > train["matches"].mean()]
train_part = train_part[["pos", "reads_all", "mismatches", "deletions", "insertions"]]

train_part.to_csv("train_part.csv")

plt.show()




