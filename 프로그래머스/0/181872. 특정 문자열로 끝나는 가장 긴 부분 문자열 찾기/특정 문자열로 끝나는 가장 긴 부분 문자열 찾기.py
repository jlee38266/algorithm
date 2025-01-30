def solution(myString, pat):
    answer = ''
    # n = len(myString)
    p = len(pat)
    
    for i in range(len(myString), p-1, -1):
    
        if myString[i-p:i] == pat:
            return myString[:i]
    
#     for i in range(n, 0, -1):
#         if i < p:
#             break
            
#         is_match = True
#         for j in range(p):
#             if myString[i-p+j] != pat[j]:
#                 is_match = False
#                 break
        
#         if is_match:
#             answer = myString[:i]
#             break
    
    return answer
