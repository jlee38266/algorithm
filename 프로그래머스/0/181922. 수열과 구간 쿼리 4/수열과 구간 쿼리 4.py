def solution(arr, queries):
    answer = arr[:]  
    
    for s,e,k in queries:
        for i in range(s, e+1):
            if k != 0 and i % k == 0:  
                answer[i] += 1
    
    return answer