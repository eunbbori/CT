# 5355번 : 화성 수학 
# @는 3을 곱하고, %는 5를 더하며, #는 7을 빼는 연산자

T = int(input())

for _ in range(T):
  S = list(map(str,input().split()))
  answer = 0 
  for i in range(len(S)):
    if i == 0:
      answer += float(S[i])
    else:
      if S[i] == '#':
        answer -= 7
      elif S[i] == '%':
        answer += 5
      elif S[i] == '@':
        answer *= 3
  print("%0.2f" % answer)   # 소수점 둘째 자리까지 출력 
