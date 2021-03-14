'''
N : 여학생
M : 남학생
K : 인턴쉽

'''

N, M, K = map(int,input().split())
woman = 0
man = 0

while 1:
    if woman > N or man > M:
        woman -= 2
        man -= 1
        break
    else:
        woman += 2
        man += 1
imsi = (N - woman) + (M - man)
while 1:
    if imsi < K:
        woman -= 2
        man -= 1
        imsi += 3
    else:
        break
print(man)
