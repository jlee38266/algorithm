def solution(myString):
    answer = []
    
    subStrings = myString.split('x')
    
    for s in subStrings:
        if s:
            answer.append(s)
            
    answer.sort()
    
    return answer