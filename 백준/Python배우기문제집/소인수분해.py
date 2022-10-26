# 11653번 : 소인수분해 

N = int(input())
#i = 2
  
if N == 1:
  print('')

for i in range(2,N+1):
  if N % i == 0: 
    while N % i == 0 :
      print(i)
      N = N // i 


# while (N != 1):
#     if N%i == 0:
#         print(i)
#         N = N//i
#     else:
#         i+=1

