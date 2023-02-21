n = int(input())
target = list(input())
answer = 0 

for _ in range(n-1):
  compare = target[:]
  word = input()
  cnt = 0 

  for w in word:
    if w in compare:
      compare.remove(w)
    else : 
      cnt += 1

  if cnt < 2 and len(compare) < 2: 
    answer += 1
print(answer)
  
#방법 2 
N = int(input())
an = 0
for i in range(N):
    A = input()
    if i == 0:
        d1 = [0 for _ in range(26)]
        for j in A:
            d1[ord(j)%65] += 1
        len1 = len(A)
        continue
    len2 = len(A)
    d2 = [0 for _ in range(26)]
    for j in A:
        d2[ord(j)%65] += 1
    a = 0
    for j in range(26):
        a += abs(d1[j]-d2[j])
    if a <= 1 or a == 2 and len1 == len2:
        an += 1
print(an)       