def solution(strArr):
    answer = 0
    len_count = {}
    
    for s in strArr:
        if len(s) in len_count:
            len_count[len(s)] += 1
        else:
            len_count[len(s)] = 1
    
    answer = max(len_count.values())
    
    return answer