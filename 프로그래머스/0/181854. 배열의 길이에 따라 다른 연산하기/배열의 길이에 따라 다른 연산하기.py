def solution(arr, n):
    # answer = []
    # arr_len = len(arr)
    
    # for i in range(arr_len):
    #     if arr_len % 2 != 0:  
    #         if i % 2 == 0:    
    #             answer.append(arr[i] + n)
    #         else:
    #             answer.append(arr[i])
    #     else:                 
    #         if i % 2 != 0:
    #             answer.append(arr[i] + n)
    #         else:
    #             answer.append(arr[i])
    # return answer
    
    for i in range(len(arr)):
        if (len(arr) % 2 == 1 and i % 2 == 0) or (len(arr) % 2 == 0 and i % 2 == 1):
            arr[i] += n
    
    return arr