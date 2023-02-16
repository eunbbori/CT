# 방법 1
def solution(s):
    answer = ''
    arr = list(map(int,s.split(" ")))
    print(arr)
    maxNum = max(arr)
    minNum = min(arr)
    answer = str(minNum)+" "+str(maxNum)
    return answer

# 방법 2
def solution(s):
    answer = ''
    arr = list(map(int,s.split(" ")))
    arr.sort()
    return str(arr[0])+" "+str(arr[-1])
