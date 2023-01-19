N = int(input())
paper = [[0]*101 for i in range(101)]

for _ in range(N):
  x,y = map(int,input().split())
  for i in range(10):
    for j in range(10):
      paper[x+i][y+j] = 1

width = 0 
for i in paper:
  width += sum(i)
print(width)