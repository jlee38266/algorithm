def solution(array):

    count_dict = {}
    
    for num in array:
        count_dict[num] = count_dict.get(num, 0) + 1
        max_count = max(count_dict.values())
    
    modes = [num for num, count in count_dict.items() if count == max_count]
    
    if len(modes) > 1:
        return -1
        
    return modes[0]