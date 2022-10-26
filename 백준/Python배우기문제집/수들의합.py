# 1789번 : 수들의 합 
S = int(input())
N = 0 
result = 0 


while N*(N+1)/2 <= S:
  N += 1 
print(N-1)  


# for i in range(1,S+1):
#   result += i
#   N += 1 
#   if(result > S):
#     N -= 1
#     break; 

# print(N)    
  

