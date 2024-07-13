# 현재 시각과 분
A, B = map(int, input().split())

# 요리 시간
C = int(input())

# 현재 시각에 요리 시간을 더하기
total_minutes = A * 60 + B + C

# 종료 시각의 시와 분을 계산
end_hour = (total_minutes // 60) % 24
end_minute = total_minutes % 60

# 종료 시각을 출력
print(end_hour, end_minute)
