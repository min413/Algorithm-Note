
# n : 떡 개수  /  m : 원하는 떡 길이
n, m = list(map(int, input().split()))

array = list(map(int, input().split()))

start = 0
end = max(array)

dap = 0

while start <= end:
    total = 0
    mid = (start + end) // 2

    for i in array:
        if i > mid:
            total += i - mid

    if total < m:
        end = mid - 1
    else:
        dap = mid
        start = mid + 1

print(dap)
