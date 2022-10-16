def main():
    N = int(input())
    S = input()

    upper = sum(i.isupper() for i in S)
    lower = sum(i.islower() for i in S)
    numbers = sum(i.isdigit() for i in S)
    
    print(upper,lower,numbers)

   
if __name__=="__main__":
    main()