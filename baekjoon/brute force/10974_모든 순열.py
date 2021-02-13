from itertools import permutations

n = int(input())
data = [i+1 for i in range(n)]

for i in list(permutations(data)):
    for j in i:
        print(j, end=' ')
    print()
