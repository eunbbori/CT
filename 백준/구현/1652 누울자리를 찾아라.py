N = int(input())
room = []
tmpCnt = 0
rowCnt = 0
colCnt = 0

for i in range(N):
    room.append(input())

for i in range(N):
    tmpCnt = 0
    for j in range(N):
        if room[i][j] == "X":
            if tmpCnt >= 2:
                rowCnt += 1
            tmpCnt = 0
        else:
            tmpCnt += 1
    if tmpCnt >= 2: #마지막 원소까지 지나왔다면
        rowCnt += 1

for i in range(N):
    tmpCnt = 0
    for j in range(N):
        if room[j][i] == "X":
            if tmpCnt >= 2:
                colCnt += 1
            tmpCnt = 0
        else:
            tmpCnt += 1
    if tmpCnt >= 2:
        colCnt += 1

print(rowCnt, colCnt)
