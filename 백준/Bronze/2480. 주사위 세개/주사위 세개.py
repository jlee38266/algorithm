def calculate_prize(a, b, c):

    if a == b == c:
        # 세 개의 주사위 눈이 모두 동일한 경우
        prize = 10000 + a * 1000
    elif a == b or b == c or a == c:
        # 두 개의 주사위 눈이 동일한 경우
        if a == b or a == c:
            prize = 1000 + a * 100
        else:
            prize = 1000 + b * 100
    else:
        # 모든 주사위 눈이 다른 경우
        prize = max(a, b, c) * 100

    return prize

# 입력: 세 개의 정수를 공백으로 구분하여 읽음
a, b, c = list(map(int, input().split()))

# 상금 계산
prize = calculate_prize(a, b, c)

# 상금 출력
print(prize)
