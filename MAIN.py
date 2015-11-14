__author__ = 'ljm7b'
import struct
from methods import *

all_roots = Roots()
root_dict = {}
my_dict = {}
level_dict = {}

trees = [[]]

for i in range(10):
    level_dict[i] = []

def optimal_binary_search_tree(keys, freq, n):
    global all_roots, level_dict, my_dict, trees
    cost = [[0] * n for i in range(n)]
    for i in range(n):
        cost[i][i] = freq[i]

    for L in range(2, n + 1):
        for i in range(0, n - L + 1):
            j = i + L - 1

            cost[i][j] = 1000000000
            roots = []
            for r in range(i, j + 1):

                c = (cost[i][r - 1] if r > i else 0) + (cost[r + 1][j] if r < j else 0) + (my_sum(freq, i, j))

                if c < cost[i][j]:
                    cost[i][j] = c

                # print('(', r + 1, ')', c, ' ', end=" ")

                roots.append((c, r + 1))
            roots.sort()

            master_root = []
            for r1 in roots:
                if r1[0] == roots[0][0]:
                    master_root.append(r1[1])

            # print('(', i + 1, '-', j+1, ')', master_root, end="   ")
            # t1 = []
            # if len(master_root) > 1:
            #     t1.append(master_root[-1])
            # else:
            #     t1.append(master_root[0])

            counter = 0
            my_dict[(i + 1, j + 1)] = []
            for rts in master_root:
                new_root = Root(rts)
                new_root.range = (i + 1, j + 1)
                new_root.calculate(i + 1, j + 1)
                new_root.node_swap()
                new_root.next_ranges.append([rts])
                all_roots.add_root(new_root)
                root_dict[new_root.range] = new_root

                sub_dict1 = {counter: {}}
                if (i + 1, j + 1) == (1, len(freq)):
                    sub_dict1[counter] = {"root": rts, "left": new_root.left, "right": new_root.right, "top": False}
                else:
                    sub_dict1[counter] = {"root": rts, "left": new_root.left, "right": new_root.right, "top": True}
                my_dict[new_root.range].append(sub_dict1[counter])
                counter += 1



    for g in all_roots.roots:
        print(g)

    # for q in all_roots.roots:
    #     if q.range == (1, 5):
    # my_dict = build_level_dict(level_dict, root_dict[(1, 5)].next_ranges, 1, root_dict)
    #         print(my_dict)
    #         for i in range(10):
    #             level_dict[i] = []
    stack1 = []
    recurse(1, 5, trees, my_dict, stack1)

    return cost[0][n - 1]


def my_sum(freq, i, j):
    s = 0
    for k in range(i, j + 1):
        s += freq[k]
    return s


keys = [10, 12, 20, 0, 0]
freq = [6, 4, 2, 6, 4]

print(optimal_binary_search_tree(keys, freq, len(freq)))
