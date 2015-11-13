
class Root(object):
    def __init__(self, root):
        self.root = root
        self.left = []
        self.right = []
        self.range = []

    def add_left(self, l=-1, r=-1):
        if l == -1 or l == r:
            self.left.append(r)
        else:
            self.left.extend([l, r])

    def add_right(self, l=-1, r=-1):
        if l == -1 or l == r:
            self.right.append(r)
        else:
            self.right.extend([l, r])

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
        return str(self.range) + "   " + str(self.left) + " " + str(self.root) + " " + str(self.right)


class Roots(object):
    def __init__(self):
        self.roots = []

    def add_root(self, root):
        self.roots.append(root)

