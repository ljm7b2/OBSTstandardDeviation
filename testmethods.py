__author__ = 'lm043536'
import random
import functools
from timeit import default_timer
from data import *



#vals = [random.randint(2000,3000) for i in range(2000)]
#vals = data()
vals = [3,3,2,1]
n = len(vals)
print("length", n)
S = [[0]*n for i in range(n)]
S2 = [[0]*n for i in range(n)]


for i in range(n):
    S[i][i] = vals[i]
    S2[i][i] = vals[i]


start = default_timer()

# for k in range(n):
#     for i in range(n):
# 	    for j in range(i+1, n):
# 	        S[i][j] = S[i][j-1] + S[i+1][j]

end = default_timer()




print("time in seconds for algo 1 iterative:", end-start)

# for line in S:
#     for c in line:
#         print(c, end=" ")
#     print()

start = default_timer()



for i in range(1, n):
    for s in range(i-1, -1, -1):
        S2[s][i] = S2[s][i-1] + S2[s+1][i]



# @functools.lru_cache(maxsize=None)
# def recurse_build(i, j):
#     global S2
#
#     if S2[i+1][j] == 0:
#         recurse_build(i+1, j)
#
#     S2[i][j] = S2[i][j-1] + S2[i+1][j]
#
#
# for i in range(n):
#     for j in range(i+1, n):
#         recurse_build(i, j)
#     break


end = default_timer()

print("time in seconds for algo 2 recursive:", end-start)

count = 0
for i in range(n):
    for j in range(n):
        if S2[i][j] != S[i][j]:
            count += 1

print("Are the results equal?", end=" ")
if count > 0:
    print("Not Equal")
else:
    print("Are Equal")



# for line in S2:
#     for c in line:
#         print(c, end=" ")
#     print()


