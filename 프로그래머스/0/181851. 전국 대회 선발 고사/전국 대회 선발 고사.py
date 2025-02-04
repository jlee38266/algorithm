def solution(rank, attendance):
    available = []
    
    for i in range(len(rank)):
        if attendance[i]:
            available.append(i)
    
    print(available)
    
    available.sort(key=lambda x:rank[x])
    a,b,c = available[:3]
    
    return 10000*a + 100*b + c