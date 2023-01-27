N = int(input())
cardList = []
discardList = []

for i in range(N):
  cardList.append(i+1)

while len(cardList) != 1 : 
  discardList.append(cardList.pop(0))
  cardList.append(cardList.pop(0))

for card in discardList: 
  print(card,end=" ")
print(cardList[0])

