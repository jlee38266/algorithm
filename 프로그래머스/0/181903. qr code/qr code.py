def solution(q, r, code):

    # return code[r::q]

    answer = ''
    
    for i in range(len(code)):
        if i % q == r:
            answer += code[i]
            
    print(answer)
    
    return answer