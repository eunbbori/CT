# 방법 1 
def solution(n, words):
    answer = []
    stack = []
    num = 0
    turn = 0
    
    stack.append(words[0])
    for i in range(1,len(words)):
        if stack[-1][-1] == words[i][0] and words[i] not in stack : 
            stack.append(words[i])
            if len(stack) ==len(words) :
                answer = [0,0]
        else : 
            num = (i % n) + 1
            turn = (i // n) + 1
            answer = [num,turn]     
            break
    return answer

#방법 2 (따로 stack에 저장할 필요가 없음)
def solution(n, words):
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i] :
            return [(i%n)+1, (i//n)+1]
    else:
        return [0,0]