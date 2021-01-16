# https://www.acmicpc.net/problem/14891

'''
N : 0
S : 1

'''

from collections import deque

data1 = deque(map(int, input()))
data2 = deque(map(int, input()))
data3 = deque(map(int, input()))
data4 = deque(map(int, input()))
# 한 data는 8개의 숫자를 가지고 있다
# data[0]은 위쪽, data[2]는 오른쪽, data[6]은 왼쪽이다
k = int(input())

dap = 0
for _ in range(k):
    saw, cur = map(int, input().split())
    cur_array = deque([cur])
    # 1번 회전시키기
    if saw == 1:
        # 1번과 2번이 다르면?
        if data1[2] != data2[6]:
            cur_array.append(-cur)
            # 2번과 3번이 다르면?
            if data2[2] != data3[6]:
                cur_array.append(cur)
                # 3번과 4번이 다르면?
                if data3[2] != data4[6]:
                    cur_array.append(-cur)
                else:
                    cur_array.append(0)
            else:
                cur_array.append(0)
                cur_array.append(0)
        else:
            cur_array.append(0)
            cur_array.append(0)
            cur_array.append(0)
    # 2번 회전시키기
    elif saw == 2:
        # 1번 2번 다르면
        if data1[2] != data2[6]:
            # cur_array의 왼쪽에 두기(처음에 있던 원소는 2번꺼의 방향이기 때문)
            cur_array.appendleft(-cur)
        else:
            cur_array.appendleft(0)
        # 2번 3번 다르면
        if data2[2] != data3[6]:
            cur_array.append(-cur)
            # 3번 4번 다르면
            if data3[2] != data4[6]:
                cur_array.append(cur)
            else:
                cur_array.append(0)
        else:
            cur_array.append(0)
            cur_array.append(0)
    # 3번 회전시키기
    elif saw == 3:
        # 2번 3번 다르면
        if data2[2] != data3[6]:
            cur_array.appendleft(-cur)
            # 1번 2번 다르면
            if data1[2] != data2[6]:
                cur_array.appendleft(cur)
            else:
                cur_array.appendleft(0)
        else:
            cur_array.appendleft(0)
            cur_array.appendleft(0)

        # 3번 4번 다르면
        if data3[2] != data4[6]:
            cur_array.append(-cur)
        else:
            cur_array.append(0)
    else:
        # 3번 4번 다르면
        if data3[2] != data4[6]:
            cur_array.appendleft(-cur)
            # 2번 3번 다르면
            if data2[2] != data3[6]:
                cur_array.appendleft(cur)
                # 1번 2번 다르면
                if data1[2] != data2[6]:
                    cur_array.appendleft(-cur)
                else:
                    cur_array.appendleft(0)
            else:
                cur_array.appendleft(0)
                cur_array.appendleft(0)
        else:
            cur_array.appendleft(0)
            cur_array.appendleft(0)
            cur_array.appendleft(0)

    data1.rotate(cur_array[0])
    data2.rotate(cur_array[1])
    data3.rotate(cur_array[2])
    data4.rotate(cur_array[3])

# 각 번호의 톱니바퀴의 12시 방향이 N극인지 확인
if data1[0] == 1:
    dap += 1
if data2[0] == 1:
    dap += 2
if data3[0] == 1:
    dap += 4
if data4[0] == 1:
    dap += 8

print(dap)
