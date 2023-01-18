from collections import deque

N,K = map(int,input().split())
queue = deque()
deleted = []


for i in range(N):
  queue.append(i+1)

while queue:
  for i in range(K-1):
    queue.append(queue.popleft())
  deleted.append(queue.popleft())

answer = ", ".join(map(str, deleted))
print('<' + answer + '>')

    