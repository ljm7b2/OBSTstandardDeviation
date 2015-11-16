from helpers import *
# define Global Variables

p = [6, 4, 2, 6, 4]
#p.extend([0 for i in range(15)])
n_max = len(p)

q = [0 for i in range(n_max)]
C = [[0]*n_max for i in range(n_max)]
W = [[0]*n_max for i in range(n_max)]
R = [[0]*n_max for i in range(n_max)]

sum_dict = sum1(p, n_max)


def compute_w_c_r():
    global p, n_max, C, W, R, sum_dict

    # construct weight matrix
    for i in range(n_max):
        W[i][i] = p[i]
        for j in range(i + 1, n_max):
            W[i][j] = W[i][j-1] + p[j]

    # construct cost, root matrix
    for i in range(n_max):
        C[i][i] = W[i][i]
        R[i][i] = i + 1

    for L in range(2, n_max + 1):
        for i in range(0, n_max - L + 1):
            j = i + L - 1

            C[i][j] = 1000000000

            for r in range(i, j + 1):
                                                                                    # this is slow makes algorithm n^4
                c = (C[i][r - 1] if r > i else 0) + (C[r + 1][j] if r < j else 0) + (my_sum(p, i, j))

                if c < C[i][j]:
                    C[i][j] = c
                    R[i][j] = r + 1


def my_sum(freq, i, j):
    print(i, j)
    s = 0
    for k in range(i, j + 1):
        s += freq[k]
    return s








# main

compute_w_c_r()

print(W)
print(C)
print(R)