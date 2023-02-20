# 방법 1
def solution(n):
    ans = 0
    while(n>1):
        if n%2 == 0 :
            n = n//2 
        else : 
            n = n-1
            ans += 1

    return ans+1

# 방법 2 
def solution(n):
    return bin(n).count('1')

