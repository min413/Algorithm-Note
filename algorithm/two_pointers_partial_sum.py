# 투 포인터 : 특정합을 가지는 부분 연속 수열 찾기

partial_sum = 5
data = [1,2,3,2,5]
end = 0
cnt = 0
interval_sum = 0

for start in range(len(data)):
    while interval_sum < partial_sum and end < len(data):
        interval_sum += data[end]
        end += 1
    if interval_sum == partial_sum:
        cnt += 1
    interval_sum -= data[start]

print(cnt)
