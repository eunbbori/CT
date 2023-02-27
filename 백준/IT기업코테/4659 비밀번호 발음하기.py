vowel = ["a","e","i","o","u"]
accept = ["ee","oo"]

while True: 
  x = 0
  y = 0
  s = input()
  if s == "end" : 
    break
  cnt = 0
  for i in vowel: 
    if i in s : 
      cnt += 1
  if cnt < 1 :
    print(f'<{s}> is not acceptable.')
    continue
  #모음만 연속 3개거나 자음만 연속 3개인 경우 체크 
  for i in range(len(s)-2) :
      if s[i] in vowel and s[i+1] in vowel and s[i+2] in vowel :
          x = 1 
      elif not(s[i] in vowel) and not(s[i+1]in vowel) and not(s[i+2] in vowel) :
          x = 1 
  if x == 1 :
    print(f'<{s}> is not acceptable.')
    continue
  #같은 글이 연속 두개인지 체크 하지만 'e'나 'o'면 컨티뉴 
  for i in range(len(s)-1) :
    if s[i]==s[i+1] :
      if s[i] == 'e' or s[i] == 'o' :
          continue
      else :
          y = 1 
  if y == 1 :
      print(f'<{s}> is not acceptable.')
      continue
  #예외 케이스를 통과하면 적합 
  print(f'<{s}> is acceptable.')