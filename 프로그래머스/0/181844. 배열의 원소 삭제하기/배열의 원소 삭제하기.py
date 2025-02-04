def solution(arr, delete_list):
    answer = []
    delete_set = set(delete_list)
    
    for num in arr:
        if num not in delete_set:
            answer.append(num)
    
    return answer