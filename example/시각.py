'''
n을 입력받아
00시 00분 00초 ~ n시 59분 59초 까지의 모든 시각 중에
3이 하나라도 포함되는 개수를 출력하여라

'''

n = int(input())
cnt = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1

print(cnt)
