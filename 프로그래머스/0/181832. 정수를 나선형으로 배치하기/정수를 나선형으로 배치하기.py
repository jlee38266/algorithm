def solution(n):
    answer = [[0]*n for _ in range(n)]
    
    x, y = 0, 0
    num = 1
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direction = 0
    
    while num <= n*n:
        answer[x][y] = num
        num += 1
    
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        if nx < 0 or nx >= n or ny >= n or answer[nx][ny] != 0:
            direction = (direction + 1) % 4
            nx = x + dx[direction]
            ny = y + dy[direction]
            
        x, y = nx, ny
    
    return answer
