N,M = map(int,input().split())
A = []
for _ in range(N):
  A.append(list(map(int,input().split())))
  
M,K = map(int,input().split())
B = []
for _ in range(M):
  B.append(list(map(int,input().split())))

C = [[0]*K for _ in range(N)]

# 방법 1
for row in range(N):
  for col in range(K):
    e = 0
    for i in range(M):
      e += A[row][i] * B[i][col]
    C[row][col] = e
for r in C :
  print(*r)

# 방법 2
# for n in range(N):
#   for k in range(K):
#     for m in range(M):
#       C[n][k] += A[n][m] * B[m][k]

# for i in C:
#   for j in i:
#     print(j,end=' ')
#   print()