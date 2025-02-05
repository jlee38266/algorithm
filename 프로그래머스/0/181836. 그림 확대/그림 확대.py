def solution(picture, k):
    answer = []
    
    for r in picture:
        print(r)
        expanded_r = ''.join(char * k for char in r)
        for _ in range(k):
            answer.append(expanded_r)
    
    return answer