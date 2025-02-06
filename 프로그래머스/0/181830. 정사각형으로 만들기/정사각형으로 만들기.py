def solution(arr):
    answer = [[]]
    rows = len(arr)
    cols = len(arr[0])
    target_size = max(rows, cols)
    
    answer = [[0] * target_size for _ in range(target_size)]
    
    for i in range(rows):
        for j in range(cols):
            answer[i][j] = arr[i][j]
            
    return answer