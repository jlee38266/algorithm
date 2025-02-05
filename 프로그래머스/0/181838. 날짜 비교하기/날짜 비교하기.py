def solution(date1, date2):
    # return 1 if date1 < date2 else 0
    
    for i in range(3):
        if date1[i] < date2[i]:
            return 1
        elif date1[i] > date2[i]:
            return 0
    return 0
