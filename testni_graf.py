import random

testna_matrika2 = [[0, 2, 3, 4, 1000],
                 [2, 0, 8, 9, 10],
                 [3, 8, 0, 14, 15],
                 [4, 9, 14, 0, 20],
                 [1000, 10, 15, 20, 0]]
n = 10
matrika1 = [[0 for col in range(n)] for row in range(n)]
random.seed(525600)
for i in range(n):
    for j in range(i+1, n):
        a = random.randint(1, 1000)
        matrika1[i][j] = a
        matrika1[j][i] = a

n = 100
matrika2 = [[0 for col in range(n)] for row in range(n)]
random.seed(525600)
for i in range(n):
    for j in range(i+1, n):
        a = random.randint(1, 1000)
        matrika2[i][j] = a
        matrika2[j][i] = a

n = 1000
matrika3 = [[0 for col in range(n)] for row in range(n)]
random.seed(525600)
for i in range(n):
    for j in range(i+1, n):
        a = random.randint(1, 1000)
        matrika3[i][j] = a
        matrika3[j][i] = a

n = 1000
matrika4 = [[0 for col in range(n)] for row in range(n)]
random.seed(525600)
for i in range(n):
    for j in range(i+1, n):
        a = random.randint(1, 1000)
        matrika4[i][j] = a
        matrika4[j][i] = a
