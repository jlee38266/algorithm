def solution(myStr):
    answer = []
    temp = ''
    
    for char in myStr:
        if char in ['a', 'b', 'c']:
            if temp:
                answer.append(temp)
                temp = ''
        else:
            temp += char
    
    if temp:
        answer.append(temp)
        
    return answer if answer else ["EMPTY"]