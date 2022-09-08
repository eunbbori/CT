S = input()
newList = []
sum = 0


for letter in S : 
  if letter.isalpha(): 
    newList.append(letter)
  else :
    sum += int(letter)

newList.sort()

if sum != 0:
  newList.append(str(sum))

print(''.join(newList))
# 최종 결과 출력(리스트를 문자열로 변환해 출력)