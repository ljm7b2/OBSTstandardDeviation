__author__ = 'ljm7b'
import struct
from methods import *

all_roots = Roots()
root_list = []


def optimal_binary_search_tree(keys, freq, n):
    global all_roots
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

            for rts in master_root:
                new_root = Root(rts)
                new_root.range.extend([i + 1, j + 1])
                new_root.calculate(i + 1, j + 1)
                all_roots.add_root(new_root)

    for g in all_roots.roots:
        print(g)
    return cost[0][n - 1]


def my_sum(freq, i, j):
    s = 0
    for k in range(i, j + 1):
        s += freq[k]
    return s


keys = [10, 12, 20, 0, 0]
freq = [6, 4, 2, 6, 4]

print(optimal_binary_search_tree(keys, freq, len(freq)))
