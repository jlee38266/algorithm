def solution(num_list):
    answer = num_list
    
    n = len(num_list)
    
    if num_list[-1] > num_list[-2]:
        result = num_list[-1] - num_list[-2]
        answer
    else:
        result = num_list[-1] * 2
    
    answer.append(result)
    print(answer)
    return answer