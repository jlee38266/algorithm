def solution(my_string, s, e):
    
    chars = list(my_string)
    
#     while s < e:
#         chars[s], chars[e] = chars[e], chars[s]
#         s += 1
#         e -= 1
    
    chars[s:e+1] = chars[s:e+1][::-1]
    
    return ''.join(chars)