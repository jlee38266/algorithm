import sys

input = sys.stdin.readline
output = sys.stdout.write

# 테스트 케이스 갯수 T 입력
T = int(input().strip())

for _ in range(T):
    A, B = map(int, input().strip().split())
    result = A + B
    output(f"{result}\n")