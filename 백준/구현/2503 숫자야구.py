from itertools import permutations
tryNum = int(input())

data = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
permuList = list(permutations(data, 3))

for _ in range(tryNum):
    num, sNum, bNum = map(int, input().split())
    num = list(str(num)) # ["1","2","3"]
    rmcnt = 0
    for i in range(len(permuList)):
        strike = ball = 0
        i -= rmcnt
        for j in range(3):
            if permuList[i][j] == num[j]:
                strike += 1
            elif num[j] in permuList[i]:
                ball += 1
            
        if (strike != sNum) or (ball != bNum):
            permuList.remove(permuList[i])
            rmcnt += 1

print(len(permuList))