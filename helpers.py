from csv import reader
from itertools import chain
from copy import deepcopy

# read and scrub data from file
# can handle multiple sets of data
def read_file(filename):
    with open(filename, newline='') as file:
        data_list, master_list = [], []
        data = reader(file, delimiter=',')
        for line in data:
            for val in line:
                if len(val) > 0:
                    num_str = ""
                    for char in val:
                        if char in "0123456789":
                            num_str += char
                    if num_str != '0':
                        data_list.append(int(num_str))
                    else:
                        master_list.append(data_list)
                        data_list = []
        master_list.append(data_list)
        return master_list


def organize_trees(trees, n_max):
    temp_tree, s1 = [], set()

    count1 = -1
    for tr in trees:
        count1 += 1
        temp_tree.append(tr)
        if count1 == n_max - 1:
            s1.add(tuple(sorted(temp_tree)))
            temp_tree = []
            count1 = -1

    trees = [list(tr) for tr in s1]

    return trees


def progress(n, n_max):
    if n == 2:
        print_progress_header()

    div = int(n_max/10)
    if n == div:
        print("\t|..10%..|")
    elif n == div * 2:
        print("\t|..20%..|")
    elif n == div * 3:
        print("\t|..30%..|")
    elif n == div * 4:
        print("\t|..40%..|")
    elif n == div * 5:
        print("\t|..50%..|")
    elif n == div * 6:
        print("\t|..60%..|")
    elif n == div * 7:
        print("\t|..70%..|")
    elif n == div * 8:
        print("\t|..80%..|")
    elif n == div * 9:
        print("\t|..90%..|")
    elif n == div * 10:
        print("\t|..100%.|")


def print_tree(trees, p, ct):
    print("Tree:", ct + 1, "-"*71)
    l1 = [(p[index], level[0], level[-1]) for index, level in enumerate(trees) if level[0] in [1, 2, 3]]
    for index, val in enumerate(l1):
        if index < 3:
            print(" -> {:>7}".format("(L:" + str(val[1]) + ", R:" + str(val[-1]) + ", " + "P:" + str(val[0]) + ")"), end="")
        elif index == 3:
            print("\n -> {:>7}".format("(L:" + str(val[1]) + ", R:" + str(val[-1]) + ", " + "P:" + str(val[0]) + ")"), end="")
        elif index < 6:
            print(" -> {:>7}".format("(L:" + str(val[1]) + ", R:" + str(val[-1]) + ", " + "P:" + str(val[0]) + ")"), end="")
        else:
            print("\n -> {:>7}".format("(L:" + str(val[1]) + ", R:" + str(val[-1]) + ", " + "P:" + str(val[0]) + ")"), end="")


    print("\n")

def print_table_info(f_name, n_max, avg1, std_dev1, wrst_case1, ct2):
    print("Tree:", ct2, "Information")
    args = [f_name, n_max, avg1[0], std_dev1,  wrst_case1]
    headers = ["FILE NAME", "N SIZE", "O(AVG)", "STD_DEV", "O(WORST)"]
    print("-"*79)
    print("{:<30s} {:<12s} {:<11s} {:<14s} {:<11s}".format(*headers))
    print("-"*79)
    print("{:<30s} {:<12d} {:<11.3f} {:<14.10f} {:<12d}".format(*args))
    print("-"*79)
    print()


def print_progress_header():
    print("Computing Optimal Binary Search Tree.....Please Wait")
    print("\t---------")