switchNum = int(input())
switchList = list(map(int,input().split()))
studentNum = int(input())

def toggle(idx):
  if switchList[idx] == 1:
    switchList[idx] = 0
  else : switchList[idx] = 1 

for st in range(studentNum):
  gender,number = map(int,input().split())
  if gender == 1:
    for i in range(1,switchNum+1):
      if(i % number == 0):
        toggle(i-1)
  if gender == 2 : 
    idx = number -1 
    toggle(idx)
    i = 1
    while number -i >= 1 and number + i <= switchNum : 
      if switchList[idx+i] == switchList[idx-i] :
        toggle(idx+i)
        toggle(idx-i)
      else : break
      i += 1


# 한 줄에 20개씩 출력 
for i in range(switchNum) : 
  print(switchList[i],end='')
  if(i+1) % 20 == 0 : # '20','40'번째 원소는 '19','39'번째 원소이기 때문에 인덱스값에 1을 더해야 
    print()
  else : print(' ', end='')  

  