studentNumList = []
tempNumList = []
studentCnt = int(input())
answerK = 0

for i in range(studentCnt):
    studentNumList.append(input())

digit = len(studentNumList[0])

for j in range(digit):
    tempNumList = []
    for i in range(studentCnt):
        num = studentNumList[i]
        sliceThing = num[digit - j - 1:digit]
        tempNumList.append(sliceThing)
    if len(tempNumList) == len(set(tempNumList)):
        print(j + 1)
        break