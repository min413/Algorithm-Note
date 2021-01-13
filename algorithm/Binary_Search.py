'''
# <이진 탐색>
# 시간 복잡도 O(logN)
# 데이터가 정렬되어 있는 상태에서 써야한다

# 재귀 함수를 이용한 이진탐색
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2 # 몫
    
    # 만약 mid 찾고자하는 데이터라면
    if array[mid] == target:
        return mid
    # mid가 찾으려는 데이터보다 크다면? -> 왼쪽으로
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # mid가 찾으려는 데이터보다 작다면? -> 오른쪽으로
    else:
        return binary_search(array, target, mid+1, end)

n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

dap = binary_search(array, target, 0, n - 1)
if dap == None:
    print("원소 없다")
else:
    print("위치는 " + str(dap+1))


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None

n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

dap = binary_search(array, target, 0, n-1)
if dap == None:
    print("원소 없다")
else:
    print("원소 위치는 " + str(dap+1))


# ============================================

# <이진 탐색 트리>
# 왼쪽 자식 < 부모 < 오른쪽 자식

# 많은 양 데이터를 빠르게 입력받는 방법 : sys 라이브러리
# rstip()은 입력된 뒤 엔터 공백문자를 없애준다
import sys
input_data = sys.stdin.readline().rstrip()

print(input_data)




'''




