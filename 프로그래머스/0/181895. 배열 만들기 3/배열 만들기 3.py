def solution(arr, intervals):
    answer = []
    
    for start, end in intervals:
        answer.extend(arr[start:end+1])
    
    return answer