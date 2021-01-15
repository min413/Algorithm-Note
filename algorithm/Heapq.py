# 출처 : https://www.daleseo.com/python-heapq/
# heapq 모듈은 최소 힙(min heap)에 동작함
# heap[k] <= heap[2*k + 1] 그리고 heap[k] <= heap[2*k + 2]
# 한 원소(k)는 항상 그 자식 원소들(2k+1, 2k+2)보다 작거나 같다

import heapq

heap = []

# 힙 원소 추가
heapq.heappush(heap, 2)
heapq.heappush(heap, 1)
heapq.heappush(heap, 6)
heapq.heappush(heap, 4)
print(heap)

'''
[1, 2, 6, 4]
인덱스 0에는 가장 작은값 1
인덱스 1(k)에 2는 인덱스 3(2k+1)에 있는 4보다 크다

시간복잡도 O(logN)
'''

# 힙 원소 삭제
print(heapq.heappop(heap)) # 삭제된 원소 리턴
print(heap)

'''
1
[2, 4, 6]

시작복잡도 O(logN)
'''

# 삭제 안하고 최소 값 얻기
print(heap[0])

'''
2

두번째로 작은 원소를 얻으려면 바로 heap[1]을 하면 안되고,
heappop()을 통해 가장 작은 원소를 삭제 후에 heap[0]을 통해 접근해야 한다


'''

# 기존 리스트를 힙으로 바꾸기

heap = [7,9,3,6,2,1,4]
heapq.heapify(heap)
print(heap)

