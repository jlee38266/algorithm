def solution(rny_string):
    answer = ''
    
    
    for char in rny_string:
        if char == 'm':
            char = 'rn'
        answer += char
    
    return answer