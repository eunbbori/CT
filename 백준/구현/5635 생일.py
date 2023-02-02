n = int(input())
studentList = [] 

for i in range(n):
  n,d,m,y = input().split()
  studentList.append([n,int(d),int(m),int(y)])
studentList.sort(key=lambda x:(x[3],x[2],x[1])) #str 안되는것 주의 

print(studentList[-1][0])
print(studentList[0][0])

  