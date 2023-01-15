N = int(input())
digitNum = len(str(N))
cnt = 0
finalDigitCnt = 0 

for i in range(digitNum-1):
  cnt += 9 * 10 ** i *(i+1)

finalDigitCnt = (N - 10 ** (digitNum-1) + 1) * digitNum 
print(cnt + finalDigitCnt) 