# 시간초과
keyWordCnt, postCnt = map(int,input().split())
wordsList = []
usedWordsList = []
answer = []
for i in range(keyWordCnt):
  wordsList.append(input())
  
for i in range(postCnt):
  usedWordsList = input().split(",")
  for j in range(2):
    if usedWordsList[j] in wordsList: 
      wordsList.remove(usedWordsList[j])
  answer.append(len(wordsList))
print(*answer,sep="\n")    


# 정답
import sys

n, m = map(int, sys.stdin.readline().split())
board = dict()
for _ in range(n) :
    board[sys.stdin.readline().rstrip()] = 1
#print(board)  # {'map': 1, 'set': 1, 'dijkstra': 1, 'floyd': 1, 'os': 1}
res = n
for _ in range(m) :
    tmp = sorted(sys.stdin.readline().rstrip().split(','))
    for t in tmp :
        if t in board.keys() :
            if board[t] == 1 :
                board[t] -= 1
                res -= 1
    print(res)  
