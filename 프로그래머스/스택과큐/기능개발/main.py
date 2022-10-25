#내 풀이 

def solution(progresses, speeds):
    answer = []
    subProgresses = []
    calProgresses = []
    cnt = 1
    result = []
    

  
    
    for i in range(len(progresses)) :
        subProgresses.append(100 - progresses[i])
        if subProgresses[i] % speeds[i] != 0 :
            calProgresses.append(subProgresses[i] // speeds[i]+ 1)
        else : 
            calProgresses.append(subProgresses[i] // speeds[i])
   
    
    for i in calProgresses : 
        if(len(result) == 0) : 
            result.append(i)
        else :    
            if (result[-1] >= i) : 
                result.append(result[-1])  
            else : 
                result.append(i)          
    
    
    temp = result[0]; 
    cnt = 0 
    for i in range(len(result)) :
        if temp != result[i] : 
                answer.append(cnt)
                cnt = 1 
                temp = result[i]
        else : 
               cnt += 1
    answer.append(cnt)       

    return answer

# 다른 사람의 풀이 1
from math import ceil

def solution(progresses, speeds):
    daysLeft = list(map(lambda x: (ceil((100 - progresses[x]) / speeds[x])), range(len(progresses))))
    count = 1
    retList = []

    for i in range(len(daysLeft)):
        try:
            if daysLeft[i] < daysLeft[i + 1]:
                retList.append(count)
                count = 1
            else:
                daysLeft[i + 1] = daysLeft[i]
                count += 1
        except IndexError:
            retList.append(count)

    return retList