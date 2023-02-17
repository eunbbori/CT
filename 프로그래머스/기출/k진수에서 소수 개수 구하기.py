import math 

def convert(num,base):
    rev_base =''
    while num > 0:
        num,mod = divmod(num,base)
        rev_base += str(mod)
    return rev_base[::-1]

def isPrime(num):
    if num == 1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0 :
            return False
    return True
        

def solution(n, k):
    answer = 0
    convertedNum = convert(n,k)
    new = str(convertedNum).split("0")
    print(new)
    for i in range(len(new)):
        if len(new[i]) == 0 :    #if new[i] == "" :
            continue
        if isPrime(int(new[i])):
            answer += 1         
    return answer