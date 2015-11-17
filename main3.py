from helpers import *
# define Global Variables

p = [26, 20, 26, 19, 26, 21, 23, 25, 28, 17, 26, 26, 29, 21, 23]
# p = [6, 4, 2, 6, 4]
# p = [16, 18, 16, 16, 22, 20, 14, 19, 14, 23, 17, 23, 15, 17]
# p = [19, 19, 20, 21, 22, 18, 21, 18, 19, 18, 22, 18, 18]

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
        node_dict[(i+1, i+1)] = [{"root": i+1, "left": -1, "right": -1}]

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
trees = []
stack = []

build_trees(1, n_max, trees, node_dict, 1, n_max)

print(W)
print(C)
print(R)
print()
# all_trees.sort()

all_trees, temp, count = [], [], -1
for tr in trees:
    count += 1
    temp.append(tr)
    if count == n_max - 1:
        all_trees.append(sorted(temp))
        temp, count = [], -1

print(all_trees)


print()
print()

for i in range(1, n_max + 1):
    for t in range(i, n_max+ 1):
        if len(node_dict[(i,t)]) > 1:
            print("(", end="")
            for s in node_dict[(i, t)]:
                print("{0:2d}".format(s["root"]), end=" ")
            print(")", end="")
        print("{0:2d}".format(node_dict[(i,t)][0]["root"]), end=" ")
    print()

