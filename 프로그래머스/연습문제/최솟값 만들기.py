def solution(A,B):
    answer = 0
    
    sortedA = sorted(A)
    sortedB = sorted(B,reverse=True)
    for i in range(len(sortedA)):
        answer += sortedA[i] * sortedB[i]
        
        

    return answer