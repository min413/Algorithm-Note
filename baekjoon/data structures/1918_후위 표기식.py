'''
<배워야 할 스킬>
딕셔너리 형태로 연산자의 순위를 정의해두고 이를 활용하기
stack[-1]으로 맨 오른쪽 원소를 구하기
stack.pop()으로 스택의 pop과 동일한 기능하기

'''
operation = {'+':1, '-':1, '*':2, '/':2, '(':0}
data = input()
imsi = [] # 후위 표기 스택
stack = [] # 연산자 스택
dap = ''

for i in data:
    if i.isalpha():
        # 알파벳이면 imsi에 넣기
        imsi.append(i)
    elif i == '(':
        # '(' 이면 stack에 넣기
        stack.append(i)
    elif i == ')':
        # 연산자 스택이 비거나 '('를 만날 때 까지 pop 진행
        while stack and stack[-1] != '(':
            imsi.append(stack.pop())
        stack.pop()
    else:
        # 현재 연산자가 스택의 top에 있는 연산자보다 우선순위가 높다면?
        while stack and operation[i] <= operation[stack[-1]]:
            imsi.append(stack.pop())
        # 현재 연산자가 스택의 top에 있는 연산자보다 우선순위가 낮거나
        # 낮은 우선순위를 가진 연산자들을 모두 pop했을 땐
        stack.append(i)

# 연산자 스택에는 한개 이상의 연산자가 있기 때문에 스택을 비운다
while len(stack) != 0:
    imsi.append(stack.pop())
for j in imsi:
    dap += j
print(dap)

