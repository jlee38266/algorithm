def solution(myString, pat):
    answer = 0
    n = len(myString)
    p = len(pat)
    
    for i in range(n-p+1):
        if myString[i:i+p] == pat:
            answer += 1
    
    return answer