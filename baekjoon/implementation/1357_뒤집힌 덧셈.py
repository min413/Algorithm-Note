'''
문자열을 int로 바꾸고 다시 str로 바꾸면 앞에 0들이 사라진다
ex) '00123' => '123'

'''

X,Y = map(str, input().split())
dap = str(int(X[::-1]) + int(Y[::-1]))
print(int(dap[::-1]))
