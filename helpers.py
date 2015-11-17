
def get_optimal_roots(root, c, i, j):
    return [rt[0] for rt in root if rt[-1] == c[i][j]]


def build_dict(i, j, roots):
    return (i, j), calculate_node(i, j, roots)


def calculate_node(i, j, roots):
    temp_dict = []
    for index, root in enumerate(roots):
        if root == i and root == j:
            temp_dict.append({"root": root, "left": -1, "right": -1, "visited": False})
        elif root == i:
            temp_dict.append({"root": root, "left": -1, "right": (root + 1, j), "visited": False})
        elif root == j:
            temp_dict.append({"root": root, "left": (i, root - 1), "right": -1, "visited": False})
        else:
            temp_dict.append({"root": root, "left": (i, root - 1), "right": (root + 1, j), "visited": False})
    return temp_dict


def my_sum(freq, i, j):
    s = 0
    for k in range(i, j + 1):
        s += freq[k]
    return s




def build_trees(i, j, trees, my_dict, level):
    for key in my_dict[(i, j)]:
        trees.append(str(key["root"]) + " L: " + str(level) + "--")
        level += 1
        if key["left"] != -1:
            build_trees(key["left"][0], key["left"][-1], trees, my_dict, level)
        if key["right"] != -1:
            build_trees(key["right"][0], key["right"][-1], trees, my_dict, level)
            trees.append("break2")
            level -= 1
            if(len(my_dict[(i, j)]) > 1) and (i, j) != (1, 5):
                my_dict[(i, j)].pop(0)


