
class Root(object):
    def __init__(self, root):
        self.root = root
        self.left = []
        self.right = []
        self.next_ranges = []
        self.range = tuple()

    def add_left(self, l=-1, r=-1):
        if l == -1 or l == r:
            self.left.extend([r, r])
        else:
            self.left.extend([l, r])
        self.next_ranges.append(self.left)

    def add_right(self, l=-1, r=-1):
        if l == -1 or l == r:
            self.right.extend([r,r])
        else:
            self.right.extend([l, r])
        self.next_ranges.append(self.right)

    def calculate(self, start, end):
        if self.root == start:
            if (self.root + 1) != end:
                self.add_right(self.root + 1, end)
            else:
                self.add_right(-1, end)

        elif self.root == end:
            if start != (self.root - 1):
                self.add_left(start, self.root - 1)
            else:
                self.add_left(-1, start)

        else:
            self.add_left(start, self.root - 1)
            self.add_right(self.root + 1, end)

    def node_swap(self):
        if len(self.right) < len(self.left):
            self.left, self.right = self.right, self.left

    def __str__(self):
        return str(self.range) + "   " + str(self.left) + " " + str(self.root) + " " + str(self.right)# + "  " + str(self.next_ranges)


class Roots(object):
    def __init__(self):
        self.roots = []

    def add_root(self, root):
        self.roots.append(root)


def build_level_dict(level_dict, next_ranges, level, next_ranges_dict):

    level += 0

    level_dict[level].append(next_ranges[-1][0])

    for i in next_ranges[:2]:
        h, s = next_ranges[:2]
        if len(i) == 0:
            continue

        elif len(h) == 1 and len(s) == 1:
            level += 1
            level_dict[level].append(h[0])
            level_dict[level].append(s[0])
            break

        elif len(i) == 1:
            level += 1
            level_dict[level].append(i[0])

        else:
            t, j = i
            # level += 1
            build_level_dict(level_dict, next_ranges_dict[(t, j)].next_ranges, level, next_ranges_dict)

    return level_dict


class Tree_Node(object):
    def __init__(self):
        self.root = 0
        self.left = 0
        self.right = 0
stack = []
level = 0
prev_level = []
big_tree = []


def recurse(i, j, trees, my_dict, stack):
    global level, prev_level, big_tree
    iter1 = ["root", "left", "right"]
    trigger = 0
    for index, key in enumerate(my_dict[(i, j)]):
        index = 0
        # level = 1
        level += 1
        for loc in iter1:

            if loc == "root":

                trees[index].append((level, key[loc]))

            elif loc == "left":

                if len(key[loc]) == 0:
                    continue

                elif len(key[loc]) == 1:
                    t1 = key[loc][0]
                    level += 1
                    trees[index].append((level, key[loc][0]))
                    level -= 1


                else:
                    recurse(key[loc][0], key[loc][-1], trees, my_dict, stack)
                    trees[index].append("break")
                    #big_tree.append(trees)
                    #trees = [[]]

            else:

                if len(key[loc]) == 0:
                    continue

                elif len(key[loc]) == 1:
                    t2 = key[loc][0]
                    level += 1
                    trees[index].append((level, key[loc][0]))
                    level -= 1


                else:
                    recurse(key[loc][0], key[loc][-1], trees, my_dict, stack)
                    trees[index].append("break")
                    print(i, j)
                    trees=[[]]

    big_tree.append(trees)
    trees = [[]]

                    #if len(my_dict[(i, j)]) > 1:
                       #level = 1

            # prev_level.append(level)

    level = 0


trees = [[] for i in range(5)]
count = 0
def recurse2(i, j, trees, my_dict, level):
    global count
    for key in my_dict[(i, j)]:


        trees[0].append((key["root"], "L: " + str(level)))
        level += 1


        if len(key["left"]) != 0:
            recurse2(key["left"][0], key["left"][-1], trees, my_dict, level)



        if len(key["right"]) != 0:
            recurse2(key["right"][0], key["right"][-1], trees, my_dict, level)


            trees[0].append("break2")


        level = 1
    level = 0



