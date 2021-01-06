from itertools import combinations

vowels = ('a', 'e', 'i', 'o', 'u')
l, c = map(int, input().split())

# 사전식으로 출력하기 위해 입력 후 정렬 수행
array = input().split()
array.sort()


for password in combinations(array, l):
    # 패스워드에 포함된 문자 중 모음 개수 확인
    cnt = 0
    for i in password:
        if i in vowels:
            cnt += 1
    # cnt는 모음 개수
    # 1개 이상 모음 and 2개 이상 자음 
    if cnt >= 1 and cnt <= l-2:
        print(''.join(password))
    # ''.join(list) : 리스트 -> 문자열 변환
