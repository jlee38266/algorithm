def solution(str_list, ex):
    answer =[]
    for s in str_list:
        if ex not in s:
            answer.append(s)
    return ''.join(answer)