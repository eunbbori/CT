def main():
   N = int(input())
   result = []

#    for _ in range(N):
#     S = input()
#     count = 0
#     for i in S:
#         if i.isupper() :
#             count += 1 
#             if count == 2 : 
#                 index = S.find(i) # WwwwwwWwwww 이 경우 안됨 
#                 result.append(S[index:])
#                 break

   for _ in range(N):
     S = input()
     count = 0
     for i in range(len(S)):
        TChar = S[i];
        if TChar.isupper() :
            count += 1 
            if count == 2 : 
                result.append(S[i:])
                break             
    
   print("\n".join(result))      
        

if __name__=="__main__":
    main()


    