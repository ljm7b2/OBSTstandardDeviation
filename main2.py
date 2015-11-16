# define Global Variables

p = [6, 4, 2, 6, 4]
#p.extend([0 for i in range(15)])
n_max = len(p)

q = [0 for i in range(n_max)]
C = [[0]*n_max for i in range(n_max)]
W = [[0]*n_max for i in range(n_max)]
R = [[0]*n_max for i in range(n_max)]



def compute_w_c_r():
    global p, n_max, C, W, R

    # construct weight matrix
    for i in range(n_max):
        W[i][i] = p[i]
        for j in range(i + 1, n_max):
            W[i][j] = W[i][j-1] + p[j]

    # construct cost, root matrix
    for i in range(n_max):
        C[i][i] = W[i][i]
        R[i][i] = i + 1

    # for i in range(n_max - 1):
    #     j = i + 1
    #     C[i][j] = C[i][i] + C[j][j] + W[i][j]
    #     R[i][j] = j

    for h in range(2, n_max + 1):
        for i in range(n_max - h + 1):
            j = i + h - 1
            m = R[i][j-1]
            min1 = C[i][m-1] + C[m][j]
            print("here",m + 1, R[i+1][j])
            for k in range(i,j+1):#m + 1, R[i+1][j]):
                x = C[i][k-1] + C[k][j]
                print(x, min1)
                if x < min1:
                    m = k
                    min1 = x
                    print(min1)

            C[i][j] = W[i][j] + min1
            R[i][j] = m


compute_w_c_r()
print(W)
print(C)
print(R)