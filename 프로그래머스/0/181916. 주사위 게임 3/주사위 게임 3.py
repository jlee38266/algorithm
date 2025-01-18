def solution(a, b, c, d):
    freq = [0] * 7
    freq[a] += 1
    freq[b] += 1
    freq[c] += 1
    freq[d] += 1
    
    
    max_freq = max(freq)
    
    if max_freq == 4:  
        for i in range(1, 7):
            if freq[i] == 4:
                return 1111 * i
                
    elif max_freq == 3:  
        p = 0  
        q = 0 
        for i in range(1, 7):
            if freq[i] == 3:
                p = i
            elif freq[i] == 1:
                q = i
        return (10 * p + q) ** 2
        
    elif max_freq == 2:
        pair_count = 0
        pairs = []
        singles = []
        
        for i in range(1, 7):
            if freq[i] == 2:
                pair_count += 1
                pairs.append(i)
            elif freq[i] == 1:
                singles.append(i)
                
        if pair_count == 2: 
            return (pairs[0] + pairs[1]) * abs(pairs[0] - pairs[1])
        else: 
            return singles[0] * singles[1]
            
    else:
        return min(a, b, c, d)