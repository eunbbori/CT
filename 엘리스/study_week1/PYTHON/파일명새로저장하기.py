def main():
    N = int(input()) 
    result = []

    for _ in range(N):
        S = input()
        lower = S.lower()
        cap = lower.capitalize()
        result.append(cap)
    
    print("\n".join(result))
    
         
    

if __name__=="__main__":
    main()


#A.capitalize 
