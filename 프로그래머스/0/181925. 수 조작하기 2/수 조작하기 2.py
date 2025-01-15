def solution(numLog):
    answer = ''
    
    value_conversion = {
        1: "w",
        -1: "s",
        10: "d",
        -10: "a"
    }
    
    for idx in range(1, len(numLog)):
        diff = numLog[idx] - numLog[idx-1]
        answer += value_conversion[diff]
    
    return answer