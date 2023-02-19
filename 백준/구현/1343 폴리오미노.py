#방법 1
s = input()
s = s.replace("XXXX","AAAA")
s = s.replace("XX","BB")

if "X" in s : 
  print(-1)
else : 
  print(s)

#방법 2
import sys

data = list(input().split("."))   #.을 기준으로 나눔
a = "AAAA"
b = "BB"

res = ""
for i in range(len(data)):
    data_len = len(data[i])
    if data_len % 2 != 0:   #안됨
        res = -1
        break
    if data_len // 4 != 0:  #몫이 0 이면 안되잖아
        res += a * (data_len // 4)
        data_len -= (data_len // 4) * 4  #사용한 만큼 지워
    if data_len // 2 != 0:  #몫이 0이면 안되니깐
        res += b * (data_len // 2)
        data_len -= (data_len // 2) * 2
    if i != len(data) -1:  #마지막에는 뒤에 .붙이니깐
        res += "."   # AAAA, BB 추가한 이후에 . 추가해줘야하니깐.

print(res)