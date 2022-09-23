def main():
    N,M = map(int,input().split())
    A = input()
    B = input()

    val = A in B 
    if val : 
        print('1')
    else : 
        print('0')     
    

if __name__=="__main__":
    main()