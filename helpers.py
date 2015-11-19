from csv import reader


# read and scrub data from file
# can handle multiple sets of data
def read_file(filename):
    with open(filename, newline='') as file:
        data_list, master_list = [], []
        data = reader(file, delimiter=',')
        for line in data:
            for val in line:
                if len(val) > 0:
                    num_str = ""
                    for char in val:
                        if char in "0123456789":
                            num_str += char
                    if num_str != '0':
                        data_list.append(int(num_str))
                    else:
                        master_list.append(data_list)
                        data_list = []
        master_list.append(data_list)
        return master_list


def organize_trees(all_trees, trees, temp, count, n_max):
    for tr in trees:
        count += 1
        temp.append(tr)
        if count == n_max - 1:
            all_trees.append(sorted(temp))
            temp, count = [], -1
    return all_trees


def progress(n, n_max):
    if n == 2:
        print_progress_header()

    div = int(n_max/10)
    if n == div:
        print("\t|..10%..|")
    elif n == div * 2:
        print("\t|..20%..|")
    elif n == div * 3:
        print("\t|..30%..|")
    elif n == div * 4:
        print("\t|..40%..|")
    elif n == div * 5:
        print("\t|..50%..|")
    elif n == div * 6:
        print("\t|..60%..|")
    elif n == div * 7:
        print("\t|..70%..|")
    elif n == div * 8:
        print("\t|..80%..|")
    elif n == div * 9:
        print("\t|..90%..|")


def print_tree(trees, p):

    for index, tree in enumerate(trees):
        print("-"*13, "Tree:", index + 1, "-"*15)
        l1, l2, l3, = [], [], []
        for level in tree:
            index = level[-1] - 1
            if level[0] == 1:
                l1.append(p[index])
            elif level[0] == 2:
                l2.append(p[index])
            elif level[0] == 3:
                l3.append(p[index])

    print("{:>20}".format(l1[0]))
    for val in l2:
        print("{:>13}".format(val), end="")
    print()
    for val in l3:
        print("{:>6}".format(val), end="   ")
    print("\n", "-"*36)

def print_table_info(f_name, n_max, avg1, std_dev1, wrst_case1):
    args = [f_name, n_max, avg1[0], std_dev1,  wrst_case1]
    headers = ["File Name", "N Size", "O(AVG)", "ST_D", "O(WRST)"]
    print()
    print("-"*78)
    print("{:<30s} {:<12s} {:<11s} {:<14s} {:<11s}".format(*headers))
    print("-"*78)
    print("{:<30s} {:<12d} {:<11.3f} {:<14.3f} {:<12d}".format(*args))
    print("-"*78)
    print()


def print_progress_header():
    print("Computing Optimal Binary Search Tree.....Please Wait")
    print("\t---------")