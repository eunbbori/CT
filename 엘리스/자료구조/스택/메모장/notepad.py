'''
notepad 함수를 작성하세요.
'''

def notepad(s, commands) :
    # 커서를 중심으로 왼쪽과 오른쪽 각각 스택에
    # 처음에는 커서가 맨 오른쪽에 있음  
    left = list(s)
    right = []

    for line in commands : 
        command = line.split() # P z 이런경우 있으니까 

        action = command[0]

        if action == "L" : 
            if len(left) > 0 : 
                v = left.pop()
                right.append(v)
        elif action == "R" :
            if len(right) > 0 :
                v = right.pop()
                left.append(v)
        elif action == "D" : 
            if len(left) > 0 : 
                left.pop()       
        elif action == "P" : 
            left.append(command[1]) 

    result = left + right[::-1]     #right 는 스택구조이기 때문에 뒤집어 줘야            


    return "".join(result)