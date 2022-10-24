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
#     for i in range(len(result)) :
#         curIndex = i 
#         if len(temp) == 0 or temp[-1] != i : 
#             curIndex = 1
#             temp.append(result[i])
#             answer.append(curIndex+1)
            
#         else : 
#             answer.pop()
#             answer.append(curIndex+1)
        
        
        
    # for i in range(len(result)-1) : 
    #     cnt = 1 
    #     if result[i] == result[i+1] and : 
    #         cnt += 1
    #         answer.append(cnt)
    #     else : 
    #         answer.append(cnt)
    return answer

    