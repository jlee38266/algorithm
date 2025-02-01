def solution(arr):
    answer = []
    target_len = 1
    
    while target_len < len(arr):
        target_len *= 2
        
    answer = arr + [0] * (target_len - len(arr))
    
    return answer