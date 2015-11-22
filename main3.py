from helpers import *
from obst_algorithms import *
from data_file import *
from memory_profiling import *
import random
from time import sleep
from timeit import default_timer as timer
from platform_info import get_platform_info
#file_names = ["CS404FS15ProjectOBSTLargeRandom(1).dat", "CS404FS15ProjectOBSTData2.dat", "CS404FS15ProjectOBSTData3.dat",
              #"CS404FS15ProjectOBSTData4.dat", "CS404FS15ProjectOBSTData5.dat", "CS404FS15ProjectOBSTData6.dat"]

file_names = ["a"]


def main(file_name):
    start = timer()
    #tracemalloc.start(25)
    # define Global Variables


    output_f = "output.txt"
    output_file = open(output_f, "a")


    #p = [6, 4, 2, 6, 4]
    #p = [1] * 500
    #p = [6,4,2,6,4]
    p = [random.randint(10, 20000) for i in range(2500)]
    #p = [3, 3, 4, 4]
    # p = [3, 2, 4, 1]
    #p = data6()



    #p = read_file(file_name) # make sure to convert to read multiple files




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
    comparisons = [0]
    # main


    compute_w_c_r(p, n_max, C, W, R, S, D, node_dict, second_best, comparisons)
    print("\n\n", file=output_file)

    total_tree_count = 0



    while ct < 2:
        build_trees(1, n_max, trees, node_dict, 1, n_max, total_tree_count, comparisons)
        ct += 1




    all_trees = organize_trees(trees, n_max)



    ct1 = 0
    print("LEVEL-ORDER TRAVERSAL   (key)->{L: Level, R: Root, P: Probability/Frequency}", file=output_file)
    for tr in all_trees[:5]:
        print_tree(tr, p, ct1, output_file)
        ct1 += 1

    avgs, std_devs = get_std_deviation(all_trees, total_sum, n_max, p)

    if len(all_trees) == 1:
        build_trees(1, n_max, trees2, second_best, 1, n_max, total_tree_count, comparisons)
        all_trees2 = organize_trees(trees2, n_max)
        print("\nTree: Second Best (Sub-Optimal Tree)", file=output_file)
        for tr in all_trees2:
            print_tree(tr, p, 0, output_file)
        avgs2, std_devs2 = get_std_deviation(all_trees2, total_sum, n_max, p)



    ct2 = 1
    print("\nIMPORT TREE INFORMATION\nOptimal Tree(s): ", len(all_trees), file=output_file)
    for i in range(len(all_trees[:5])):
        print_table_info(file_name, n_max, avgs[i], std_devs[i], all_trees[i][-1][0], ct2, output_file)
        ct2 += 1
    if len(all_trees) == 1:
        print("\nSecond Best Tree (Sub-Optimal)", file=output_file)
        print_table_info(file_name, n_max, avgs2[0], std_devs2[0], all_trees2[0][-1][0], 1, output_file)



    # print("COMPUTING MEMORY DIAGNOSTICS......")
    # print("Please be patient, this could take some time!")

    #snapshot = tracemalloc.take_snapshot()
    #display_top(snapshot)

    # OR

    #snapshot = tracemalloc.take_snapshot()
    #top_stats = snapshot.statistics('lineno')

    # print("[ Top 10 ]")
    # for stat in top_stats[:5]:
    #     print(stat)


    #print(W)
    #print(C)
    #print(R)
    #print("std", std_devs)

    #print("t1 == t2?", all_trees[0] == all_trees[1])

    # get_platform_info()

    print("Total Comparisons:", comparisons[0], file=output_file)

    end = timer()
    print("Total Computation Time: {:4.2f}".format(end - start), "seconds", file=output_file)
    print("Total Computation Time: {:4.2f}".format((end - start) / 60), "minutes", file=output_file)
    print("\n\n\n", file=output_file)
    output_file.close()
    #sleep(10)
    #snapshot = tracemalloc.take_snapshot()
    #display_top(snapshot)

for f in file_names:
    main(f)