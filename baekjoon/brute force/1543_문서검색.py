'''
앞에서부터 찾고자하는 단어있지 검사
만약 같다면 찾은 글자수만큼은 잘라내기
다르다면 맨 앞 한 글자만 잘라내기

'''
data = input()
want = input()
dap = 0

while 1:
    check = 0
    if len(data) >= len(want):
        for i in range(len(want)):
            if data[i] != want[i]: # 하나라도 다르다면 check에 1 넣기
                check = 1
    else:
        break
    
    if check == 0: # 일치한다면?
        dap += 1
        data = data[len(want):]
    else: # 다르다면?
        data = data[1:]

print(dap)
        


