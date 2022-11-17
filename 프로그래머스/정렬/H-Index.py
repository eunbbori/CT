def solution(citations):
    answer = 0
    temp = []

    citations.sort()
    print(citations)
    for i in range(len(citations)) : 
        if citations[i] >= len(citations)-i : 
            return len(citations)-i
    return 0
