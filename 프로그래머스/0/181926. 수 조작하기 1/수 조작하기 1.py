def solution(n, control):
    answer = n
    
#     for char in control:
#         if char == "w":
#             answer += 1
#         elif char == "s":
#             answer -= 1
#         elif char == "d":
#             answer += 10
#         elif char == "a":
#             answer -= 10

    control_val = {
        "w": 1,
        "s": -1,
        "d": 10,
        "a": -10
    }
    
    for char in control:
        answer += control_val[char]
    
    return answer