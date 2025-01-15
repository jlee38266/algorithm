def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        min_val = float('inf')
        
        for i in range(s, e+1):
            if arr[i] > k and arr[i] < min_val:
                min_val = arr[i]
        
        answer.append(-1 if min_val == float('inf') else min_val)
    print(answer)
    return answer