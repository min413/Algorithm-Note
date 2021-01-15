# https://www.acmicpc.net/problem/18406
# 계속 문자열의 각 인덱스를 가져오는 문법이 c랑 헷갈린다
# 파이썬으로 간단한 문제들이라도 익숙해지도록 풀어봐야겠다
import sys

def total(str):
    a = 0
    for i in str:
        a += int(i)
    return a

    
data = sys.stdin.readline().rstrip()
length = len(data) // 2
left = data[:length]
right = data[length:]

if total(left) == total(right):
    print("LUCKY")
else:
    print("READY")
