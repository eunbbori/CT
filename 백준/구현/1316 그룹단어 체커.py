# 방법 1
wordsNum = int(input())
groupWordCnt = 0

for i in range(wordsNum):
  word = input()
  error = 0 
  for index in range(len(word)-1):
    if word[index] != word[index+1]: # 문자열이 연달아있는 경우 신경쓸 필요가 없다 
      new_word = word[index+1:]
      if new_word.count(word[index]) > 0:
        error += 1

  if error == 0:
    groupWordCnt += 1
print(groupWordCnt)

# 방법 2
wordsNum = int(input())
groupWordCnt = wordsNum

for i in range(wordsNum):
  word = input()
  for j in range(len(word)-1):
    if word[j] == word[j+1]:
      pass
    elif word[j] in word[j+1:]:
      groupWordCnt -= 1
      break
print(groupWordCnt)