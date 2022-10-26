# 1934번 : 최소공배수 
T = int(input())

def gcd(A,B):  #최대공약수 구하기
  for i in range(min(A,B),0,-1):
    if A % i==0 and B % i ==0:
      return i 


for i in range(T):
  A,B = map(int,input().split())
  print((A*B) // gcd(A,B))  



# 유클리드 호제법으로 구하기
# def gcd(x, y):  #최대공약수 구하기
#   if y == 0:
#     return x
#   else:
#     return gcd(y, x%y)
  
# def lcm(x, y):  ## 최소공배수 구하기
#   result = (x*y) // gcd(x,y)
#   return result

# num = int(input())

# for i in range(num):
#   x, y = map(int, input().split(" "))
#   print(lcm(x, y))


