from output_methods import *
from memory_profiling import *


file_name = "CS404FS15ProjectOBSTData6.dat"  # <- define your file name here please, include extension

prob = read_file(file_name)


def main():
    global prob, file_name

    for p in prob:
        # define global variables
        n_max = len(p)
        total_sum = sum(p)
        q = [0 for i in range(n_max)]
        C = [[0]*n_max for i in range(n_max)]
        W = [[0]*n_max for i in range(n_max)]
        R = [[0]*n_max for i in range(n_max)]
        S = [[0]*n_max for i in range(n_max)]
        node_dict, count, trees, recheck, ct = {}, 0, [], [1], 0
        second_best, trees2 = {}, []
        comparisons = [0]
        # tracemalloc.start()  #  <- memory profiling (TAKES FOREVER!, uncomment two lines at bottom too)
        start = timer()
        total_tree_count = 0
        output_f = "output.txt"
        output_file = open(output_f, "a")

        # compute the weight cost and root matrices and node_dictionaries
        compute_w_c_r(p, n_max, C, W, R, S, node_dict, second_best, comparisons)

        # get top five trees
        while ct < 5:
            build_trees(1, n_max, trees, node_dict, 1, n_max, total_tree_count, comparisons)
            ct += 1

        all_trees = organize_trees(trees, n_max)

        # get standard deviation as well as expected average
        avgs, std_devs = get_std_deviation(all_trees, total_sum, n_max, p)

        # display information nicely
        print_main(output_file, all_trees, n_max, trees2, second_best, total_tree_count, comparisons, total_sum,
                   file_name, p, avgs, std_devs, start)

        output_file.close()

        # snapshot = tracemalloc.take_snapshot()  # <- memory profiling and line below
        # display_top(snapshot)


main()

print("Complete, Your output is ready in file: output.txt")
print("NOTE: This file is set to 'APPEND', multiples sets will be appended.")