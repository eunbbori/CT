bingo = []
targets = []
count = 0 

for i in range(5):
  bingo.append(list(map(int,input().split())))
for i in range(5):
  targets.append(list(map(int,input().split())))
def solution(array:list):
  bingo_number = 0 
  #가로가 빙고일때 
  for i in range(5):
    if sum(array[i]) == 0 :
      bingo_number += 1
  #세로가 빙고일때
  for i in range(5):
    count_temp = 0
    for j in range(5):
      if array[j][i] == 0:
        count_temp += 1
    if count_temp == 5:
      bingo_number += 1
  #대각선이 빙고일때
  temp_up = []
  temp_down = []
  for i in range(5):
    temp_up.append(array[i][i])
    temp_down.append(array[i][4-i])
  if sum(temp_up) == 0:
    bingo_number += 1
  if sum(temp_down) == 0:
    bingo_number += 1

  return bingo_number

      
for i in range(5):
  for j in range(5):
    for k in range(5):
      for h in range(5):
        if targets[i][j] == bingo[k][h]:
          bingo[k][h] = 0 
          count += 1
        if count >= 12: # 3빙고가 나오기 위한 최소한의 조건
          if solution(bingo) >= 3: # 빙고개수 3 이상
            print(count)
            exit()