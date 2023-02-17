def solution(s):
    answer = []
    newStr = s.strip("{""}")  # 2},{2,1},{2,1,3},{2,1,3,4
    newStr2 = newStr.replace("},{",",") #	2,2,1,2,1,3,2,1,3,4
    finalStrList = list(map(int,newStr2.split(','))) #	[1, 2, 3, 2, 1, 1, 2, 4, 3, 2]
    
    dic = {n:0 for n in set(finalStrList)} # {1: 0, 2: 0, 3: 0, 4: 0}
    for n in finalStrList : 
        dic[n] += 1                        #{ 1: 3, 2: 4, 3: 2, 4: 1}
    dic = sorted(dic.items(),key=lambda x: x[1],reverse=True) #	[(2, 4), (1, 3), (3, 2), (4, 1)]
    return [k for k, v in dic]