def solution(my_string, queries):
    chars = list(my_string)
    
    for s, e in queries:
        while s < e:
            chars[s], chars[e] = chars[e], chars[s]
            s += 1
            e -= 1
    
    return ''.join(chars)