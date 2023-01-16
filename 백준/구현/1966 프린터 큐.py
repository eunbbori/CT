testCase = int(input())
priorities = []
answer = 0
answerList = []

for i in range(testCase):
  N, M = list(map(int,input().split()))
  priorities = list(map(int,input().split()))
  queue = [(index,p) for index,p in enumerate(priorities)]
  while True:
    cur = queue.pop(0)
    if any(cur[1] < q[1] for q in queue):
      queue.append(cur)
    else :
      answer += 1
      if cur[0] == M :
        answerList.append(answer)
        answer = 0 
        queue = []
        break
print("\n".join(map(str,answerList)))
  
    
  
  
    
