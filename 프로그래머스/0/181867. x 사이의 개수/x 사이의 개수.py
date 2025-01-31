def solution(myString):
    answer = []
    
    substrings = myString.split('x')
    
    for str in substrings:
        answer.append(len(str))
    
    return answer