'''
우선 화폐는 오름차순으로 정렬
타겟을 1부터 잡아 화폐들 중에서 타겟보다 작다면 그 화폐를 그냥 타겟에 더하고
다음 화폐로 넘어간다
이때 타겟보다 더 큰 화폐가 있다면 그 금액이 답이다

그리디를 많이 풀면 금방 풀이가 보인다고 하니깐 많이 풀어봐야겠다..

'''

n = int(input())

data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x:
        break
    else:
        target += x

print(target)
