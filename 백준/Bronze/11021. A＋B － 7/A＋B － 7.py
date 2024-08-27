import sys

input = sys.stdin.readline

# 테스트 케이스 갯수 T 입력
T = int(input().strip())

for i in range(1, T + 1):
    A, B = map(int, input().split())
    result = A + B
    print(f"Case #{i}: {result}")