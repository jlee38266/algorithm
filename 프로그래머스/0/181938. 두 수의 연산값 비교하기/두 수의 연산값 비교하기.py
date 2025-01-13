def solution(a, b):
    answer = 0
    
    ab = int(str(a) + str(b))
    two_ab = 2 * a * b
    
    if ab > two_ab:
        answer = ab
    else:
        answer = two_ab
    
    return answer