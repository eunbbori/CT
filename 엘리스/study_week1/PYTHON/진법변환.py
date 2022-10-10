def main():
    N,B = map(int,input().split(' '))

    def baseSolution(n,b):
        rev_base=''

        if n==0: 
            return 0 

        while n>0 :
            n,mod = divmod(n,b) #두 숫자를 인자로 전달 받아 첫번째 인자를 두번째 인자로 나눈 몫과 나머지를 tuple 형식으로 반환한다. 
            rev_base += str(mod)

        return rev_base[::-1]    

    print(baseSolution(N,B))    

      

if __name__=="__main__":
    main()