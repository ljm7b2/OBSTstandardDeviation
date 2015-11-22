from data_file import *
from output_methods import *
from memory_profiling import *
import random
from platform_info import get_platform_info

file_names = ["CS404FS15ProjectOBSTLargeRandom(1).dat", "CS404FS15ProjectOBSTData2.dat", "CS404FS15ProjectOBSTData3.dat",
              "CS404FS15ProjectOBSTData4.dat", "CS404FS15ProjectOBSTData5.dat", "CS404FS15ProjectOBSTData6.dat"]

# define Global Variables
p = [6, 4, 2, 6, 4]
#p = [random.randint(10, 20000) for i in range(1500)]
#p = data1()
#p = read_file(file_name) # make sure to convert to read multiple files

n_max = len(p)
total_sum = sum(p)
q = [0 for i in range(n_max)]
C = [[0]*n_max for i in range(n_max)]
W = [[0]*n_max for i in range(n_max)]
R = [[0]*n_max for i in range(n_max)]
S = [[0]*n_max for i in range(n_max)]
# D = [[0]*n_max for i in range(n_max)]
node_dict, count, trees, recheck, ct = {}, 0, [], [1], 0
second_best, trees2 = {}, []
comparisons = [0]


def main(file_name):
    global n_max, p, total_sum, q, C, W, R, S, \
        node_dict, count, trees, recheck, ct, \
        second_best, trees2, comparisons
    # tracemalloc.start()
    start = timer()
    total_tree_count = 0
    output_f = "output.txt"
    output_file = open(output_f, "w")

    compute_w_c_r(p, n_max, C, W, R, S, node_dict, second_best, comparisons)

    while ct < 2:
        build_trees(1, n_max, trees, node_dict, 1, n_max, total_tree_count, comparisons)
        ct += 1

    all_trees = organize_trees(trees, n_max)

    avgs, std_devs = get_std_deviation(all_trees, total_sum, n_max, p)

    print_main(output_file, all_trees, n_max, trees2, second_best, total_tree_count, comparisons, total_sum,
               file_name, p, avgs, std_devs, start)

    output_file.close()

    # snapshot = tracemalloc.take_snapshot()
    # display_top(snapshot)

for f in file_names[:1]:
    main(f)