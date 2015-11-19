from helpers import *
from obst_algorithms import *
from data_file import *
import time
import random
from timeit import default_timer as timer
start = timer()
# define Global Variables

file_name = "file.txt"

# p = [26, 20, 26, 19, 26, 21, 23, 25, 28, 17, 26, 26, 29, 21, 23]
p = [6, 4, 2, 6, 4]
#p = [16, 18, 16, 16, 22, 20, 14, 19, 14, 23, 17, 23, 15, 17]
# p = [19, 19, 20, 21, 22, 18, 21, 18, 19, 18, 22, 18, 18]
# p = [1234, 1234, 1234, 1234, 1234, 1234, 1234, 1234, 1234, 1234, 1234, 1234, 1234, 1234]
# p = [random.randint(1000, 2000) for i in range(2000)]
# p = [10, 3, 9, 2, 0, 10]
#p = [3, 3, 4, 4]
# p = [3, 2, 4, 1]
# p = data()

t = read_file("test.txt")




n_max = len(p)
total_sum = sum(p)
q = [0 for i in range(n_max)]
C = [[0]*n_max for i in range(n_max)]
W = [[0]*n_max for i in range(n_max)]
R = [[0]*n_max for i in range(n_max)]
S = [[0]*n_max for i in range(n_max)]
D = [[0]*n_max for i in range(n_max)]
node_dict, count, trees, recheck, ct = {}, 0, [], [1], 0
all_trees = []
# main

print("Computing Optimal Binary Search Tree.....Please Wait")
print("\t---------")
compute_w_c_r(p, n_max, C, W, R, S, D, node_dict)
print("\t---------")

while len(trees) < 3:
    build_trees(1, n_max, trees, node_dict, 1, n_max)
    ct += 1

#if trees[0] == trees[-1]:
    #trees.pop(-1)

all_trees = organize_trees(all_trees, trees, [], -1, n_max)

#print("Trees", all_trees)

for tr in all_trees:
    print_tree(tr, p)
    print()
    print()


print()
print(len(all_trees))

avgs, std_devs = get_std_deviation(all_trees, total_sum, n_max, p)

#print(W)
#print(C)
#print(R)
print()

end = timer()
print("Time elapsed:", end - start, "seconds")
print("Time elapsed:", (end - start)/ 60, "minutes")

print_table_info(file_name,n_max,avgs[0],std_devs[0],all_trees[0][-1][0])