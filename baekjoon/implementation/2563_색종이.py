'''
1. 처음엔 전체 넓이에서 겹쳐지는 영역의 넓이를 빼는 방법을 생각했지만
색종이 개수가 100개는 된다는 조건이 있어 이것은 아니었음을 깨닳았고
인터넷 검색을 통해 2차원 좌표를 이용하는 방법을 알아냈다

2. 101 x 101개의 원소를 모두 탐색하도 되지만, (10201 이니깐)

'''

n = int(input())
data = [[0 for _ in range(101)] for _ in range(101)]
for _ in range(n):
    a,b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            data[i][j] = 1

dap = 0
for c in data: # 2차원 배열 중 행만 가져다 쓰기
    dap += c.count(1) # 가져온 행에 1의 개수를 세어준다
print(dap)
