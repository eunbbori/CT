def main():

    N = int(input())
    S = input()
    M = int(input())

    SArr = list(map(int,S.split(' ')))
    count = 0

    for i in SArr:
        if i == M :
            count += 1 
        
    
    print(count)    
    

    # print(N)
    # print(S)
    # print(M)


if __name__=="__main__":
    main()