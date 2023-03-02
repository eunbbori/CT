import math
import itertools

def isPrime(num):
    for i in range(2,int(math.sqrt(num)) + 1):
        if num % i == 0 :
            return False
    return True

def solution(nums):
    answer = 0
    primeNum = []
    
    for i in itertools.combinations(nums,3):
        primeNum.append(sum(i))
    for i in primeNum:
        if isPrime(i):
            answer += 1
        else : 
            continue
    return answer