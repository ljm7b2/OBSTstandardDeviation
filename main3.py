from helpers import *
import time
import random
from timeit import default_timer as timer
start = timer()
# define Global Variables

# p = [26, 20, 26, 19, 26, 21, 23, 25, 28, 17, 26, 26, 29, 21, 23]
p = [6, 4, 2, 6, 4]
#p = [16, 18, 16, 16, 22, 20, 14, 19, 14, 23, 17, 23, 15, 17]
# p = [19, 19, 20, 21, 22, 18, 21, 18, 19, 18, 22, 18, 18]
#p = [4 for i in range(250)]
# p = [10, 3, 9, 2, 0, 10]
#p = [3, 3, 4, 4]
# p = [3, 2, 4, 1]





n_max = len(p)
total_sum = sum(p)
q = [0 for i in range(n_max)]
C = [[0]*n_max for i in range(n_max)]
W = [[0]*n_max for i in range(n_max)]
R = [[0]*n_max for i in range(n_max)]
S = [[0]*n_max for i in range(n_max)]
node_dict, count, trees, recheck, ct = {}, 0, [], [1], 0
all_trees = []
# main

print("Computing tables")
compute_w_c_r(p, n_max, C, W, R, S, node_dict)


while ct < recheck[0]:
    build_trees(1, n_max, trees, node_dict, 1, n_max, recheck)
    ct += 1

all_trees = organize_trees(all_trees, trees, [], -1, n_max)

print(all_trees)
print(len(all_trees))
print(get_std_deviation(all_trees, total_sum, n_max))

print(W)
print(C)
print(R)
print()



# for i in range(1, n_max + 1):
#     for t in range(i, n_max+ 1):
#         if len(node_dict[(i,t)]) > 1:
#             print("(", end="")
#             for s in node_dict[(i, t)]:
#                 print("{0:2d}".format(s["root"]), end=" ")
#             print(")", end="")
#         print("{0:2d}".format(node_dict[(i, t)][0]["root"]), end=" ")
#     print()

end = timer()
print("Time elapsed:", end - start, "seconds")
print("Time elapsed:", (end - start)/ 60, "minutes")