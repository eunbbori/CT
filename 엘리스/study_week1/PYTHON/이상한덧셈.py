def main():
    N = int(input())
    for _ in range(N):
        A,B = list(map(str,input().split(' ')))
        EliceA = A[::-1]
        EliceB = B[::-1]
        sum = int(EliceA) + int(EliceB)
        result = str(sum)[::-1]
        print(result)

if __name__=="__main__":
    main()