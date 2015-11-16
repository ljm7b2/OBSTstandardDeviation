def sum1(freq, n_max):
    s = 0
    sum_dict = {}
    for i in range(n_max):
        for k in range(i + 1, n_max):
            for l in range(i, k):
                s += freq[l]
            sum_dict[(i, k)] = s
            s = 0
    return sum_dict