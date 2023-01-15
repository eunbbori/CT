peopleCnt = int(input())
peopleList = []

for i in range(peopleCnt):
  weight, height = map(int,input().split())
  peopleList.append((weight, height))

for i in peopleList:
  rank = 1
  for j in peopleList:
    if i[0] < j[0] and i[1] < j[1]:
      rank += 1
  print(rank,end=" ")
  