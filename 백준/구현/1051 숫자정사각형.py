height, width = map(int,input().split())
map =[]

for i in range(height):
  map.append(list(input()))

squareWidth = min(height,width)
answer = 0
for i in range(height):
  for j in range(width):
    for k in range(squareWidth):
      if((i+k)<height) and ((j+k)<width) and (map[i][j] == map[i][j+k] == map[i+k][j] == map[i+k][j+k]):
        answer = max(answer,(k+1)**2)
print(answer)