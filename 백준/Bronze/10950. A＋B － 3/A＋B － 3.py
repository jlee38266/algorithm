# 테스트 케이스의 반복 횟수 지정
T = int(input())

# 각 테스트 케이스마다 2개의 input 값을 받고 덧셈 연산
for _ in range(T):
    A, B = map(int, input().split())
    print(A + B)