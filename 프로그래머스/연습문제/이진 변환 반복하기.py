def solution(s):
    answer = []
    totalDumped = 0
    totalTobin = 0
    while( s != "1"):
        if '0' in s:
            totalDumped += s.count('0')
            s = s.replace("0","")
            
        s = str(format(len(s),'b'))
        totalTobin += 1
        
        
    answer = [totalTobin,totalDumped]

    return answer