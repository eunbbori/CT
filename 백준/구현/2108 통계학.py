from collections import Counter

N = int(input())
numberList = []
for i in range(N):
    numberList.append(int(input()))


def mean(arr):
    numSum = sum(arr)
    meanVal = round(numSum / N)
    if meanVal <0 and meanVal >-1 :
      print(0)
    else:
      print(meanVal)


def median(arr):
    arr.sort()
    index = N // 2
    print(arr[index])


def mode(arr):
    count = Counter(arr)
    order = count.most_common()  #등장한 횟수를 내림차순으로 정리
    max = order[0][1]

    modes = []
    for i in order:
        if (i[1] == max):
            modes.append(i[0])

    if len(modes) <= 1:
        print(modes[0])
    else:
        print(modes[1])


def maxMin(arr):
    maxNum = max(arr)
    minNum = min(arr)
    print(maxNum - minNum)


mean(numberList)
median(numberList)
mode(numberList)
maxMin(numberList)
