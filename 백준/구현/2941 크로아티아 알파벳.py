word = input()
wordList = ["c=","c-","dz=","d-","lj","nj","s=","z="]

for i in wordList:
  word = word.replace(i,'*')
print(len(word))
