'''
1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19

'''

E, S, M = map(int, input().split())
cnt = 0
E_cnt = 1
S_cnt = 1
M_cnt = 1
while 1:
    if E_cnt == 16:
        E_cnt = 1
    if S_cnt == 29:
        S_cnt = 1
    if M_cnt == 20:
        M_cnt = 1
    cnt += 1
    if E_cnt == E and S_cnt == S and M_cnt == M:
        print(cnt)
        break
    E_cnt += 1
    S_cnt += 1
    M_cnt += 1
    
    
    
    
