def solution(num_list, n):
    answer = []
    
    # answer = num_list[n:] + num_list[:n]
    for i in range(len(num_list)):
        answer.append(num_list[(i + n) % len(num_list)])
    
    return answer