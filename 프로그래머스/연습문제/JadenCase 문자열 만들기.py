def check(s):
    if type(s[0]) == int :     # if ord(s[0]) >=48 and ord(s[0]) <=57 : 
        s = s.lower()
    else : 
        s = s.capitalize()
    return s
            
            
def solution(s):
    answer = ''
    answerArr = []
    splitArr = s.split(" ")
    for i in splitArr:
        if i != "": 
            new = check(i)
            answerArr.append(new)
        elif i == "":
            answerArr.append("")
    answer = ",".join(answerArr).replace(","," ")      
    return answer