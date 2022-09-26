def main(): 
    N = int(input())
    cnt = 0 
    result = []
    
    for i in range(1,N+1):
        if N % i == 0 : 
            cnt += 1 
            result.append(i)
    result.insert(0,cnt)
    for j in result : 
        print(j)
        
    #print("\n".join(map(str,result)))
        


if __name__=="__main__":
    main()