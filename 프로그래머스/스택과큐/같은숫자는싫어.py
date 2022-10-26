#나의 풀이 

def solution(arr):
    answer = []

    for i in range(len(arr)) : 
        if i == 0 :
            answer.append(arr[i])
        else :     
            if(arr[i-1] != arr[i]) : 
                answer.append(arr[i]) 

    return answer


#다른 사람의 풀이 

def no_continuous(s):
    result = []
    for c in s:
        if (len(result) == 0) or (result[-1] != c):
            result.append(c)
    return result

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( no_continuous( "133303" ))