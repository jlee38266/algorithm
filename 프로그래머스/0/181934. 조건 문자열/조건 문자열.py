def solution(ineq, eq, n, m):
    answer = 0
    
    if ineq + eq == ">=":
        return int(n >= m)
    elif ineq + eq == "<=":
        return int(n <= m)
    elif ineq + eq == ">!":
        return int(n > m)
    else:
        return int(n < m)
            
    return answer