from sys import stdin

N = int(stdin.readline())
people = list(map(int,stdin.readline().split()))
check = [0] * N

for i in range(N):
    cnt = 0
    for j in range(N):
        if cnt == people[i] and check[j] == 0:
            check[j] = i + 1
            break
        elif check[j] == 0:
            cnt += 1
for i in check:
    print(i, end=" ")