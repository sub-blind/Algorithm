n = int(input())
target = int(input())

grid = [[0]*n for _ in range(n)]
x, y = 0, 0
num = n*n
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dir = 0
tx, ty = 0, 0

while num > 0:
    grid[x][y] = num
    if num == target:
        tx, ty = x+1, y+1
    nx = x + dx[dir]
    ny = y + dy[dir]
    if nx < 0 or nx >= n or ny < 0 or ny >= n or grid[nx][ny] != 0:
        dir = (dir + 1) % 4
        nx = x + dx[dir]
        ny = y + dy[dir]
    x, y = nx, ny
    num -= 1

for row in grid:
    print(' '.join(map(str, row)))
print(tx, ty)
