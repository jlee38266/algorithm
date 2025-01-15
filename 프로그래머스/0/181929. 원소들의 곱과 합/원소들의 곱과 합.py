def solution(num_list):
    answer = 0
    case1 = 0
    case2 = 1
    
    for num in num_list:
        case1 += num
        case2 *= num
    # print(case1**2)
    # print(case2)
    if case1**2 > case2:
        answer = 1
        
    return answer
