T = int(input())

def binary_search(array, target, start, end):
    while(start <= end):
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for _ in range(T):
    N = int(input())
    data_1 = list(map(int, input().split()))
    M = int(input())
    data_2 = list(map(int, input().split()))
    data_1.sort()

    for i in data_2:
        print(binary_search(data_1, i, 0, N-1))
