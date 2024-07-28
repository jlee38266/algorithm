# 총 금액
X = int(input())

# 물건 종류 수
N = int(input())

# 총 금액 초기화
cal_total = 0

# 총 금액 계산
for _ in range(N):
    a, b = map(int, input().split())
    cal_total += a * b
    
# 금액 비교
if cal_total == X:
    print("Yes")
else:
    print("No")

