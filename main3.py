from helpers import *
from obst_algorithms import *
from data_file import *
from memory_profiling import *
import random
from timeit import default_timer as timer
from platform_info import get_platform_info
start = timer()
tracemalloc.start()
# define Global Variables

file_name = "file.txt"
output_file = "output.txt"


p = [6, 4, 2, 6, 4]
#p = [6,4,2,6,4]
# p = [random.randint(1000, 2000) for i in range(500)]
#p = [3, 3, 4, 4]
# p = [3, 2, 4, 1]
# p = data2()

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
second_best, trees2 = {}, []

# main


compute_w_c_r(p, n_max, C, W, R, S, D, node_dict, second_best)
print("\n\n")

total_tree_count = 0

while ct < 30:
    build_trees(1, n_max, trees, node_dict, 1, n_max, total_tree_count)
    ct += 1




all_trees = organize_trees(trees, n_max)



ct1 = 0
print("LEVEL-ORDER TRAVERSAL   (key)->{L: Level, R: Root, P: Probability/Frequency}")
for tr in all_trees:
    print_tree(tr, p, ct1)
    ct1 += 1

avgs, std_devs = get_std_deviation(all_trees, total_sum, n_max, p)

if len(all_trees) == 1:
    build_trees(1, n_max, trees2, second_best, 1, n_max, total_tree_count)
    all_trees2 = organize_trees(trees2, n_max)
    print("Tree: Second Best (Sub-Optimal Tree")
    for tr in all_trees2:
        print_tree(tr, p, 0)
    avgs2, std_devs2 = get_std_deviation(all_trees2, total_sum, n_max, p)



ct2 = 1
print("IMPORT TREE INFORMATION\nOptimal Tree(s): ", len(all_trees))
for i in range(len(all_trees)):
    print_table_info(file_name, n_max, avgs[i], std_devs[i], all_trees[i][-1][0], ct2)
    ct2 += 1
if len(all_trees) == 1:
    print("Second Best Tree (Sub-Optimal")
    print_table_info(file_name, n_max, avgs2[0], std_devs2[0], all_trees2[0][-1][0], 1)

end = timer()
print("Time elapsed:", end - start, "seconds")
print("Time elapsed:", (end - start) / 60, "minutes")

print("COMPUTING MEMORY DIAGNOSTICS......")
print("Please be patient, this could take some time!")

#snapshot = tracemalloc.take_snapshot()
#display_top(snapshot)

# OR

#snapshot = tracemalloc.take_snapshot()
#top_stats = snapshot.statistics('lineno')
#
# print("[ Top 10 ]")
# for stat in top_stats[:5]:
#     print(stat)


#print(W)
#print(C)
#print(R)
#print("std", std_devs)

#print("t1 == t2?", all_trees[0] == all_trees[1])

get_platform_info()