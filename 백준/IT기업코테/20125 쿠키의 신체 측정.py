N = int(input())
map = []

for _ in range(N):
  map.append(list(input().rstrip()))

# map ex 
# [['_', '_', '_', '_', '_'], ['_', '_', '*', '_', '_'], ['_', '*', '*', '*', '_'], ['_', '_', '*', '_', '_'], ['_', '*', '_', '*', '_']]

heart = False
x = 0
y = 0 
for i in range(N):
  for j in range(N):
    if map[i][j] == "*":
      x = i+2
      y = j+1
      print(x,y)
      heart = True
      break
  if heart :
    break

left_arm = 0
for i in range(y-1):
  if map[x-1][i] == "*" : 
    left_arm += 1

right_arm = 0 
for i in range(y,N):
  if map[x-1][i] == "*": 
    right_arm += 1

back = 0 
line = 0 
for i in range(x,N):
  if map[i][y-1] == "*":
    back += 1
    line = i

left_leg = 0
for i in range(N-1,line,-1):
  if map[i][y-2] == "*": 
    left_leg += 1

right_leg = 0
for i in range(N-1,line,-1):
  if map[i][y] == "*" : 
    right_leg += 1
print(left_arm,right_arm,back,left_leg,right_leg)