from obst_algorithms import *
from timeit import default_timer as timer
from platform_info import *


def print_main(output_file, all_trees, n_max, trees2, second_best, total_tree_count, comparisons, total_sum,
               file_name, p, avgs, std_devs, start):
    print("\n\n", file=output_file)
    ct1 = 0
    print("LEVEL-ORDER TRAVERSAL   (key)->{L: Level, R: Root, P: Probability/Frequency}", file=output_file)
    print("Tree(s): Optimal Tree(s)", file=output_file)
    for tr in all_trees[:5]:
        print_tree(tr, p, ct1, output_file)
        ct1 += 1

    if len(all_trees) == 1:
        build_trees(1, n_max, trees2, second_best, 1, n_max, total_tree_count, comparisons)
        all_trees2 = organize_trees(trees2, n_max)
        print("\n\nTree: Second Best (Sub-Optimal Tree)", file=output_file)
        for tr in all_trees2:
            print_tree(tr, p, 0, output_file)
        avgs2, std_devs2 = get_std_deviation(all_trees2, total_sum, n_max, p)

    ct2 = 1
    print("\n\nIMPORTANT TREE INFORMATION\n\nOptimal Tree(s): ", len(all_trees), file=output_file)
    for i in range(len(all_trees[:5])):
        print_table_info(file_name, n_max, avgs[i], std_devs[i], all_trees[i][-1][0], ct2, output_file)
        ct2 += 1
    if len(all_trees) == 1:
        print("\nSecond Best Tree (Sub-Optimal)", file=output_file)
        print_table_info(file_name, n_max, avgs2[0], std_devs2[0], all_trees2[0][-1][0], 1, output_file)

    print("\nTotal Comparisons:", comparisons[0], file=output_file)

    end = timer()
    print("Total Computation Time: {:4.2f}".format(end - start), "seconds", file=output_file)
    print("Total Computation Time: {:4.2f}".format((end - start) / 60), "minutes", file=output_file)
    get_platform_info(output_file)
    print("\n\n\n", file=output_file)
