def solution(a, b, c):
    answer = 0
    combi1 = a + b + c
    combi2 = (a**2 + b**2 + c**2)
    combi3 = (a**3 + b**3 + c**3) 
    
    if a == b and b == c:
        answer = combi1 * combi2 * combi3
    elif a == b or b == c or a == c:
        answer = combi1 * combi2
    else:
        answer = combi1
    
    return answer