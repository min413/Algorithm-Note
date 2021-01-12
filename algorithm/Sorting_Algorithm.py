'''
# <선택 정렬>
# 무작위로 배열된 데이터 중 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 
# 그 자음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸고...
# 매번 가장 작은 것을 선택한다는 의미에서 "선택정렬"
# 가장 작은 데이터를 앞으로 보내는 과정을 n-1번 반복하면 끝난다
# 시간 복잡도는 (N-1) + (N-2) + ... 2 = N x (N+1)/2
# O(N^2)
# 비효율적이지만 익숙할 정도로 외워둘 것

array = [7,5,9,0,3,1,6,2,4,8]
for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index] , array[i] # 스와프
print(array)

# ===================================================

# <삽입 정렬>
# 두 번째 데이터부터 탐색하여 앞 데이터들 중 적절한 위치에 삽입한다
# 이때 앞 데이터들은 정렬되어있다고 가정 (실제로도 정렬되어있다)
# 정렬은 항상 오름차순이 유지됨
# 삽입될 데이터가 들어갈 위치를 찾으려고 왼쪽으로 움직일 때 마다 자기보다 작은 데이터를 만나면 그 자리에서 멈추면 된다
# 시간복잡도는 O(N^2)
# 선택 정렬과 비슷한 시간복잡도이지만 데이터가 정렬되어 있는 상태에선 빠르게 동작한다
# 최선의 경우 O(N)까지 가능
# 심지어 거의 정렬된 상태에서는 퀵 정렬보다 빠르다!


array = [7,5,9,0,3,1,6,2,4,8]
for i in range(1, len(array)):
    # 인덱스 i부터 1(0+1)까지 감소하며 반복됨
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else :
            break

print(array)

# ===================================================

# <퀵 정렬>
# 기준을 정한 후 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작한다
# 피벗(pivot) == 기준
# 시간 복잡도는 O(NlogN) 최악에 경우는 O(N^2)
# 퀵 정렬은 이미 정렬되어 있는 경우 매우 느리게 동작한다
# (삽입 정렬은 정렬 되어있을 때 매우 빠름)


array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    # 원소가 1개면 종료
    if start >= end:
        return
    
    # 피벗은 첫번째 원소
    pivot = start
    left = start + 1
    right = end
    
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지
        while right > start and array[right] >= array[pivot]:
            right -= 1
        
        if left > right:
            # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:
            # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array,start, right-1)
    quick_sort(array,right+1, end)

quick_sort(array,0,len(array) - 1)
print(array)

# 퀵 정렬의 다른 소스코드

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    # 리스트가 하나이하 원소만 가지면 종료
    if len(array) <= 1:
        return array

    pivot = array[0] # 피벗 = 첫번째 원소
    tail = array[1:] # 피벗 제외 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분 둘다 정렬을 수행하고 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

# ===================================================

# <계수 정렬>
# 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르다
# 데이터 개수 N, 데이터 최대값 K일 때, 시간복잡도는 최악이라도 O(N+K)
# 단, 데이터 크기 범위가 제한되어 정수형태로 표현할 수 있을 때만 사용 가능
# (대략 1,000,000 넘지 않을 때)
# 왜냐하면 배열을 선언하기 때문
# 앞서 데이터들을 비교하고 값을 비교하는 알고리즘들과 달리,
# 별도의 리스트를 선언하고 그 안에 정렬에 대한 정보를 담는다
# 하지만 공간복잡도가 심각하게 비효율적
# 공간복잡도 O(N+K)


# 모든 원소 값이 0보다 크거나 같다 (인덱스는 0 이상 정수이기 때문)
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

cnt = [0] * (max(array) + 1)

for i in range(len(array)):
    cnt[array[i]] += 1

for i in range(len(cnt)):
    for j in range(cnt[i]):
        print(i, end=' ')

# ===================================================

# <파이썬의 정렬 라이브러리>
# 기본 정렬 라이브러리 sorted()는 퀵 정렬과 비슷한 병합 정렬으로 기반됨
# 병합 정렬은 퀵 정렬보다는 느리지만, 최악이라도 시간 복잡도 O(NlogN)을 보장한다
# 집합, 딕셔너리 자료형을 입력받아도 결과는 리스트 자료형

array = [7,5,9,0,3,1,6,2,4,8]
dap = sorted(array)
print(dap)

array = [7,5,9,0,3,1,6,2,4,8]
array.sort()
print(array)


# key 매개변수를 입력으로 받을 수 있다
# key 값으로 하나의 함수가 들어가고 이게 정렬 기준이 됨
array = [('바나나', 2), ('사과', 5), ('당근', 3)]
def setting(data):
    return data[1]

dap = sorted(array, key=setting)
print(dap)

'''
