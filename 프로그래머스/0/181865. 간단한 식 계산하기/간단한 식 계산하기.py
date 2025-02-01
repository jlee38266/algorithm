def solution(binomial):
    
    a, op, b = binomial.split()
    
    num1 = int(a)
    num2 = int(b)
    
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    else:
        return num1 * num2