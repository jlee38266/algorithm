def solution(a, d, included):
    answer = 0
#     result = []
    
#     for i in range(len(included)):
#         current = a + d*i
#         result.append(current)
        
#         if included[i]:
#             answer += current

    for i in range(len(included)):
        if included[i]:
            answer += a + d*i
    
    return answer