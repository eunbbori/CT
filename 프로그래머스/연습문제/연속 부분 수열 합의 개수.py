# 방법 1
def solution(elements):
    cycle = elements + elements
    s = set()
    for i in range(len(elements)):
        for j in range(len(elements)):
            s.add(sum(cycle[i:i+j]))
            # print("i: ",i)
            # print("j: ",j)
            # print("sum: ",sum(cycle[i:i+j]))
            # print("s: ",s)
            # print("-------")
    return len(s)

# 방법 2 
from collections import deque
 
def solution(elements):
    answer = set()
    elements = deque(elements)
    for j in range(len(elements)):
        elements.rotate(1)
        # print("rotate elements: ", elements)
        for i in range(1,len(elements)):
            answer.add(sum(list(elements)[:i]))
            # print("sum", sum(list(elements)[:i]))
    answer.add(sum(elements))
    
    return len(answer)