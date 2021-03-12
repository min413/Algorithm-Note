n = int(input())
if n == 1:
    print("*")
else:
    for i in range(n):
        if i%2 != 0:
            print(' ', end='')
        for _ in range(n-1):
            print('* ', end='')
        print('*')
