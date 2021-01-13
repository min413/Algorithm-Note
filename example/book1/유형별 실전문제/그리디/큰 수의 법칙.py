'''
다양한 수로 이루어진 배열에서 주어진 수들을 m번 더하여
특정 인덱스에 해당하는 수가 연속해서 k번을 초과하지 않는 한도에서
더해지지 않는 방식으로 더해질 수 있는 가장 큰수를 구하여라

'''
n, m, k = map(int, input().split()) # int 변수가 공백구분해서 입력받는 코드

array = list(map(int, input().split())) # list 형식으로 받기(정렬하기 위해서)

array.sort(reverse = True)
first = array[0]
second = array[1]

dap = 0

repeat = m // (k+1) # 한 구간이 반복되는 개수
cnt = repeat * k # 가장 큰 수(first)가 더해지는 개수 구하는 과정
cnt += m % (k+1)

dap += cnt * first # first들 더하기
dap += (m - cnt) * second # second들 더하기

print(dap)




