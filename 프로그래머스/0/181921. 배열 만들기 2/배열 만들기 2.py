def solution(l, r):
    answer = []
    
    def check_zero_five(num):
        while num > 0:
            digit = num % 10
            if digit != 0 and digit != 5:
                return False
            num //= 10
        return True

    for num in range(l, r+1):
        if check_zero_five(num):
            answer.append(num)
    
    return answer if answer else [-1]