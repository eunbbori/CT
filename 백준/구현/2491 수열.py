#방법 1
N = int(input())
seq = list(map(int,input().split()))
prev = seq[0]
min_cnt = 1
max_cnt = 1
ans = 1

for i in seq[1:]:
  if i>= prev:
    min_cnt += 1
  else : 
    min_cnt = 1
  if i <= prev:
    max_cnt += 1
  else : 
    max_cnt = 1
  prev = i
  ans = max(ans,min_cnt,max_cnt)
print(ans)

#방법 2
def check(nums):
  global ans
  cnt = 1
  for i in range(1,N):
    if nums[i-1] <= nums[i] : 
      cnt += 1
    else : 
      cnt = 1
    if ans < cnt :
      ans = cnt 

N = int(input())
seq = list(map(int,input().split()))

ans = 1

check(seq)
check(seq[::-1])
print(ans)
