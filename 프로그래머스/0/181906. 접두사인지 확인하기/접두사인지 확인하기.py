def solution(my_string, is_prefix):
    prefix_list = []
    
    
    for i in range(1, len(my_string)+1):
        prefix_list.append(my_string[:i])
    
    print(prefix_list)
    
    if is_prefix in prefix_list:
        return 1
    else:
        return 0
