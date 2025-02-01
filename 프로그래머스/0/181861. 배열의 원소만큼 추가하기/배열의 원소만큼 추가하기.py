def solution(arr):
    answer = []
    
    # for num in arr:
    #     answer += [num] * num
        
    for num in arr:  
        for _ in range(num):
            answer.append(num)
            
    return answer
