from helpers import *
from math import sqrt


def compute_w_c_r(p, n_max, C, W, R, S, D, node_dict, second_best_dict, comparisons):

    # construct weight matrix
    for i in range(n_max):
        W[i][i] = p[i]
        for j in range(i + 1, n_max):
            W[i][j] = W[i][j-1] + p[j]
    # construct cost, root matrix
    for i in range(n_max):
        C[i][i] = W[i][i]
        R[i][i] = i + 1
        S[i][i] = p[i]
        node_dict[(i+1, i+1)] = [{"root": i+1, "left": -1, "right": -1}]
        second_best_dict[(i+1, i+1)] = [{"root": i+1, "left": -1, "right": -1}]
    for i in range(1, n_max):
        for s in range(i-1, -1, -1):
            S[s][i] = S[s][i-1] + S[s+1][i] - S[s+1][i-1]
    for L in range(2, n_max + 1):
        progress(L, n_max)
        for i in range(0, n_max - L + 1):
            j = i + L - 1
            C[i][j] = 1000000000
            roots = []
            for r in range(R[i][j-1]-1, R[i+1][j]+1):
                c = (C[i][r - 1] if r > i else 0) + (C[r + 1][j] if r < j else 0) + S[i][j]
                comparisons[0] += 3
                if c < C[i][j]:
                    C[i][j] = c
                    R[i][j] = r + 1
            # get all optimal roots and build root data dictionary (map)
                roots.append((c, r + 1))
            optimal_roots, sub_optimal_roots = sort_roots(roots, C[i][j], comparisons)

            loc, sub_dict = build_dict(i+1, j+1, optimal_roots)
            node_dict[loc] = sub_dict

            loc2, sub_dict2 = build_dict(i+1, j+1, sub_optimal_roots)
            second_best_dict[loc2] = sub_dict2


def build_trees(i, j, trees, my_dict, level, size, total_trees, comparisons):
    for key in my_dict[(i, j)]:
        trees.append((level, key["root"]))
        level += 1
        if key["left"] != -1:
            build_trees(key["left"][0], key["left"][-1], trees, my_dict, level, size, total_trees, comparisons)
            comparisons[0] += 1
        if key["right"] != -1:
            build_trees(key["right"][0], key["right"][-1], trees, my_dict, level, size, total_trees, comparisons)
            comparisons[0] += 1
            level -= 1
            if(len(my_dict[(i, j)]) > 1) and (i, j) != (1, size):
                comparisons[0] += 2
                my_dict[(i, j)].pop(0)
                total_trees += 1


def get_optimal_roots(root, c, i, j):
    return [rt[0] for rt in root if rt[-1] == c[i][j]]


def build_dict(i, j, roots):
    return (i, j), calculate_node(i, j, roots)


def calculate_node(i, j, roots):
    temp_dict = []
    for root in roots:
        if root == i and root == j:
            temp_dict.append({"root": root, "left": -1, "right": -1})
        elif root == i:
            temp_dict.append({"root": root, "left": -1, "right": (root + 1, j)})
        elif root == j:
            temp_dict.append({"root": root, "left": (i, root - 1), "right": -1})
        else:
            temp_dict.append({"root": root, "left": (i, root - 1), "right": (root + 1, j)})
    return temp_dict


def get_std_deviation(all_trees, total_sum, n_max, probabilities):
    temp_sum1, temp_sum2, sum_list, counter = 0, 0, [], 1
    for t in all_trees:
        for node in t:
            depth, index = node
            temp_sum1 += depth * (probabilities[index-1] / total_sum)
            temp_sum2 += (depth ** 2) * (probabilities[index-1] / total_sum)
            if counter == n_max:
                sum_list.append((temp_sum1, temp_sum2))
                temp_sum1, temp_sum2, counter = 0, 0, 0
            counter += 1
    return sum_list, [sqrt(val[-1] - (val[0] ** 2)) for val in sum_list]


def sort_roots(roots, min_val, comparisons):
    min_roots = []
    second_root = [(10000000000000000000000, 1)]
    for val in roots:
        if val[0] == min_val:
            min_roots.append(val[-1])
        else:
            second_root.append(min(second_root.pop(), val))
        comparisons[0] += 2
    return min_roots, [second_root[0][-1]]



