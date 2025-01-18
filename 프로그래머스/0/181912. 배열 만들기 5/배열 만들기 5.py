def solution(intStrs, k, s, l):
    answer = []
    
    for string in intStrs:
        # print(string)
        substr = string[s:s+l]
        # print(substr)
        num = int(substr)
        
        if num > k:
            answer.append(num)
    
    return answer