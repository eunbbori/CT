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

