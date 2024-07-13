# 현재 알람 시간 입력 받기
H, M = map(int, input().split())

# 45분 앞당기기
if M >= 45:
    M -= 45
else:
    M += 15  # M = M + 60 - 45
    if H > 0:
        H -= 1
    else:
        H = 23

# 결과 출력
print(H, M)