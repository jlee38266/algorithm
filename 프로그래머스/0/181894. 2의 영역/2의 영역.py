def solution(arr):
    left, right = 0, len(arr) - 1
    
    while left <= right and arr[left] != 2:
        left += 1
        
    while left <= right and arr[right] != 2:
        right -= 1
        
    if left > right:
        return [-1]
        
    return arr[left:right + 1]