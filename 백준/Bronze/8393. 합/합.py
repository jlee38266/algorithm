n = int(input())

# 합 변수 초기화
sum = 0

# 1 ~ n까지 모든 숫자를 반복하면서 합 (stop 부분은 포함되지 않기 때문에 n + 1로 설정)
for i in range(1, n + 1):
    sum += i

# 모든 합의 결과 출력
print(sum)