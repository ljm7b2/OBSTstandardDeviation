
class Root(object):
    def __init__(self, root):
        self.root = root
        self.left = []
        self.right = []
        self.next_ranges = []
        self.range = tuple()

    def add_left(self, l=-1, r=-1):
        if l == -1 or l == r:
            self.left.append(r)
        else:
            self.left.extend([l, r])
        self.next_ranges.append(self.left)

    def add_right(self, l=-1, r=-1):
        if l == -1 or l == r:
            self.right.append(r)
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

    def __str__(self):
        return str(self.range) + "   " + str(self.left) + " " + str(self.root) + " " + str(self.right) + "  " + str(self.next_ranges)


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


