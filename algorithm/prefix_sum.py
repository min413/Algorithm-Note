# 접두사의 합을 이용한 구간 합 계산

data = [10, 20, 30, 40, 50]
N = len(data)


sum = 0
prefix_sum = [0]
for i in data:
    sum += i
    prefix_sum.append(sum)

left = 3
right = 4

print(prefix_sum[right] - prefix_sum[left-1])

# 데이터 : 10 20 30 40 50
# 접두사 합 :  0    10   30   60  100  150
#            P[0] P[1] P[2] P[3] P[4] P[5]
