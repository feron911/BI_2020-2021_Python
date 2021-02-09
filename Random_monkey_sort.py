import random as rnd
import matplotlib.pyplot as plt
import time

def sorted_list(li:list):
    if len(li) == 0:
        return "List is empty"
    if len(li) == 1:
        return "List has only one element. This list is totally sorted."
    for i in range(len(li) - 1):
        if li[i] > li[i + 1]:
            #print("List is NOT sorted")
            return False
    #print("List is sorted")
    return True

lirnd = []
len_of_list = []
time_of_sort = []
for i in range (2, 12):
    len_of_list.append(i)
    lirnd = [rnd.randint(-100, 100) for _ in range(i)]
    print(lirnd)
    start = time.time()
    while not sorted_list(lirnd):
        rnd.shuffle(lirnd)
    time_of_sort.append(time.time() - start)
    lirnd = []
plt.plot(len_of_list, time_of_sort)
plt.ylabel("time of sort")
plt.xlabel("len of list")
print(time_of_sort, len_of_list)

plt.show()







