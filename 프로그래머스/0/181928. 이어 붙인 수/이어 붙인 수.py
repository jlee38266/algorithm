def solution(num_list):
    answer = 0
    even = 0
    odd = 0
    
    for num in num_list:
        if num % 2 == 0:
            even = even * 10 + num
        else:
            odd = odd * 10 + num
            
    answer = even + odd
    
    return answer