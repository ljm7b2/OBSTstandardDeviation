from helpers import *
# define Global Variables

p = [6, 4, 2, 6, 4]

n_max = len(p)

q = [0 for i in range(n_max)]
C = [[0]*n_max for i in range(n_max)]
W = [[0]*n_max for i in range(n_max)]
R = [[0]*n_max for i in range(n_max)]

# sum_dict = sum1(p, n_max)

node_dict = {}


def compute_w_c_r():
    global p, n_max, C, W, R, node_dict

    # construct weight matrix
    for i in range(n_max):
        W[i][i] = p[i]
        for j in range(i + 1, n_max):
            W[i][j] = W[i][j-1] + p[j]

    # construct cost, root matrix
    for i in range(n_max):
        C[i][i] = W[i][i]
        R[i][i] = i + 1
        node_dict[(i+1, i+1)] = [{"root": i+1, "left": -1, "right": -1, "visited": False}]

    for L in range(2, n_max + 1):
        for i in range(0, n_max - L + 1):
            j = i + L - 1

            C[i][j] = 1000000000
            roots = []
            for r in range(i, j + 1):
                                                                                    # this is slow makes algorithm n^4
                c = (C[i][r - 1] if r > i else 0) + (C[r + 1][j] if r < j else 0) + (my_sum(p, i, j))

                if c < C[i][j]:
                    C[i][j] = c
                    R[i][j] = r + 1

            # get all optimal roots and build root data dictionary (map)
                roots.append((r + 1, c))
            loc, sub_dict = build_dict(i+1, j+1, [rt[0] for rt in roots if rt[-1] == C[i][j]])
            node_dict[loc] = sub_dict



# main

compute_w_c_r()

count = 0
all_trees = []
stack = []

build_trees(1, n_max, all_trees, node_dict, 1)

print(W)
print(C)
print(R)
print()
for line in all_trees:

        if line == "break2":
            print("\n")
        else:
            print(line, end=" ")