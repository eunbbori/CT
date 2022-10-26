# 나의 풀이 
def solution(s):
    answer = True
    stack  = []
 
    for i in range(len(s)) : 
        if s[i] == '(' : 
            stack.append(s[i])
        else: 
            if len(stack) == 0 : 
                return False
            stack.pop()
   
    if len(stack) == 0 : 
        return True
    else :
        return False 
   


# 다른 사람의 풀이 1
def is_pair(s):
    # 함수를 완성하세요
    open_cnt = 0
    for c in s:
        if c == '(':
            open_cnt += 1
        elif c == ')':
            open_cnt -= 1
            if open_cnt < 0:
                return False
    return open_cnt == 0


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( is_pair("(hello)()"))
print( is_pair(")("))

# 다른 사람의 풀이 2
def is_pair(s):
    st = list()
    for c in s:
        if c == '(':
            st.append(c)

        if c == ')':
            try:
                st.pop()
            except IndexError:
                return False

    return len(st) == 0


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(is_pair("(hello)()"))
print(is_pair(")(()))"))
