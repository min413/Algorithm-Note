N, M = map(int, input().split())
package = []
piece = []

for _ in range(M):
    a, b = map(int,input().split())
    package.append(a)
    piece.append(b)

package.sort()
piece.sort()
imsi = 0
dap = 0

if N >= 6:
    imsi = N//6
    N = N%6
    dap = dap + min(package[0]*imsi, piece[0]*imsi*6)

dap = dap + min(package[0], piece[0] * N)
print(dap)
