# most 1 

def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

# most 2 : deque 사용 

from collections import deque
def solution(priorities, location):
    index_list = deque([i for i in range(len(priorities))])
    maximum = max(priorities)
    answer = 0
    while True:
        index = index_list.popleft()
        if priorities[index] < maximum:
            index_list.append(index)
        else:
            answer += 1
            priorities[index] = 0
            maximum = max(priorities)
            if index == location:
                return answer

