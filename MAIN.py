__author__ = 'ljm7b'
import itertools
from copy import deepcopy
from methods import *
import random

import cProfile
import re
cProfile.run('re.compile("main()")')

all_roots = Roots()
root_dict = {}
my_dict = {}
level_dict = {}

ij_list = []

all_roots_list = []
trees = [[] for i in range(5)]

for i in range(10):
    level_dict[i] = []

def optimal_binary_search_tree(keys, freq, n):
    global all_roots, level_dict, my_dict, trees
    cost = [[0] * n for i in range(n)]
    root = [[0] * n for i in range(n)]
    combo_roots = []
    counter = 0
    sub_dict1 = {counter: {}}
    for i in range(n):
        cost[i][i] = freq[i]
        root[i][i] = i + 1
        sub_dict1[counter] = {"root": i + 1, "left": [], "right": [], "range": (i + 1, i + 1)}
        my_dict[(i + 1, i + 1)] = []
        my_dict[(i+1, i+1)].append(sub_dict1[counter])
    print("here3")
    for L in range(2, n + 1):
        for i in range(0, n - L + 1):
            j = i + L - 1

            cost[i][j] = 1000000000
            roots = []
            for r in range(i, j + 1):

                c = (cost[i][r - 1] if r > i else 0) + (cost[r + 1][j] if r < j else 0) + (my_sum(freq, i, j))

                if c < cost[i][j]:
                    cost[i][j] = c
                    root[i][j] = r + 1
                    print(cost[i][j], i+1, j+1)

                print('(', r + 1, ')', c, ' ', end=" ")

                roots.append((c, r + 1, (i, j)))
            roots.sort()


            master_root = []
            for r1 in roots:
                if r1[0] == roots[0][0]:
                    master_root.append(r1[1])
            if len(master_root) > 1:

                combo_roots = []
                for i12 in master_root:
                    combo_roots.append(i12)
                all_roots_list.append(combo_roots)

                ij_list.append([i, j])

            print('(', i + 1, '-', j+1, ')', master_root, end="   ")
    print("here4")
    m1 = list(itertools.product(*all_roots_list))

    t5 =[]
    for i in range(len(m1)):
        t5.append(deepcopy(root))

    for index, val in enumerate(m1):   # build all grid combinations in a list
        counter = 0
        for s5 in val:
            t5[index][ij_list[counter][0]][ij_list[counter][-1]] = s5
            counter += 1

    ss1 = []
    root_dict = {}
    all_roots = Roots()
    super_list_1 = []
    print("here5")
    for root2 in t5:
        #my_dict = {}
        for L in range(2, n + 1):
            for i in range(0, n - L + 1):
                j = i + L - 1
                my_dict[(i + 1, j + 1)] = []
                new_root = Root(root2[i][j])
                new_root.range = (i + 1, j + 1)
                new_root.calculate(i + 1, j + 1)
                new_root.node_swap()
                new_root.next_ranges.append([root2[i][j]])
                all_roots.add_root(new_root)
                root_dict[new_root.range] = new_root


                sub_dict1 = {counter: {}}
                if (i + 1, j + 1) == (1, len(freq)):
                    sub_dict1[counter] = {"root": root2[i][j], "left": new_root.left, "right": new_root.right, "top": False, "range": (i + 1, j + 1)}
                else:
                    sub_dict1[counter] = {"root": root2[i][j], "left": new_root.left, "right": new_root.right, "top": True, "range": (i + 1, j + 1)}
                my_dict[(i + 1, j + 1)].append(sub_dict1[counter])
                counter += 1

            #print(root_dict)

        recurse2(1, n, trees, my_dict, 1)
        super_list_1.append(trees)
        trees = [[]]

    return cost[0][n - 1]


def my_sum(freq, i, j):
    s = 0
    for k in range(i, j + 1):
        s += freq[k]
    return s


keys = [10, 12, 20, 0, 0]
freq = [6, 4, 2, 6, 4]


freq_test = []
def main():
    # for i in range(50):
    #     freq_test.append(random.randint(0, 25))
    freq_test = [5, 5, 5, 15, 10, 10, 10]
    optimal_binary_search_tree(keys, freq_test, len(freq_test))



main()