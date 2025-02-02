def solution(num_list):
    # return sorted(num_list)[:5]

    def quick_sort(arr, start, end):
        if start >= end: 
            return
        
        pivot = start
        left = start + 1
        right = end
        
        while left <= right:
            while left <= end and arr[left] <= arr[pivot]:
                left += 1
            while right > start and arr[right] >= arr[pivot]:
                right -= 1
                
            if left > right:
                arr[right], arr[pivot] = arr[pivot], arr[right]
            else:
                arr[left], arr[right] = arr[right], arr[left]
                
        quick_sort(arr, start, right-1)
        quick_sort(arr, right+1, end)
    
    arr = num_list.copy()
    quick_sort(arr, 0, len(arr)-1)
    return arr[:5]