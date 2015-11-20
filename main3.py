from helpers import *
from obst_algorithms import *
from data_file import *
from memory_profiling import *
import random
from timeit import default_timer as timer
start = timer()
tracemalloc.start()
# define Global Variables

file_name = "file.txt"
output_file = "output.txt"


#p = [6, 4, 2, 6, 4]
#p = [random.randint(1000, 2000) for i in range(500)]
#p = [3, 3, 4, 4]
# p = [3, 2, 4, 1]
p = data6()

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

# main


compute_w_c_r(p, n_max, C, W, R, S, D, node_dict)
print("\n\n")

while ct < 30:
    build_trees(1, n_max, trees, node_dict, 1, n_max)
    ct += 1

#if trees[0] == trees[-1]:
    #trees.pop(-1)

all_trees = organize_trees(trees, n_max)

#print("Trees", all_trees)

ct1 = 0
print("LEVEL-ORDER TRAVERSAL")
for tr in all_trees:
    print_tree(tr, p, ct1)
    ct1 += 1



#print()
#print(len(all_trees))

avgs, std_devs = get_std_deviation(all_trees, total_sum, n_max, p)

#print(W)
#print(C)
#print(R)
#print("std", std_devs)

#print("t1 == t2?", all_trees[0] == all_trees[1])

ct2 = 1
print("IMPORT TREE INFORMATION")
for i in range(len(all_trees)):
    print_table_info(file_name, n_max, avgs[i], std_devs[i], all_trees[i][-1][0], ct2)
    ct2 += 1

end = timer()
print("Time elapsed:", end - start, "seconds")
print("Time elapsed:", (end - start) / 60, "minutes")

print("COMPUTING MEMORY DIAGNOSTICS......")
print("Please be patient, this could take some time!")

# snapshot = tracemalloc.take_snapshot()
# display_top(snapshot)

# OR

#snapshot = tracemalloc.take_snapshot()
#top_stats = snapshot.statistics('lineno')
#
# print("[ Top 10 ]")
# for stat in top_stats[:5]:
#     print(stat)