def main():
    N = int(input())
    startNum = 1 
    result = 0
    answer = 0 
    for _ in range(N):
        c,x = list(map(str,input().split()))
        if c == '+' : 
            result = startNum + int(x) 
            startNum = result
        elif c == '-': 
            result = startNum - int(x) 
            startNum = result
        else :
            result = startNum * int(x)       
            startNum = result
    answer = result  % 1000000007  
    print(answer)        

        

if __name__=="__main__":
    main()