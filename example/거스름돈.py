'''
거스름돈 N원을 500원, 100원, 50원, 10원짜리 동전들로 줄 수 있는
동전 개수가 최소가 되도록 하여라
'''

N = int(input())
cnt = 0
coins = [500, 100, 50, 10]

for coin in coins:
    cnt += N // coin
    N %= coin

print(cnt)
