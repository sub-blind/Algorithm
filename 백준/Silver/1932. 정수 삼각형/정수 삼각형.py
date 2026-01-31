size = int(input())

triangle = []
for _ in range(size):
    triangle.append(list(map(int, input().split())))

result = []
for row in range(size):
    result.append([0] * (row + 1))

result[0][0] = triangle[0][0]

for row in range(1, size):
    for col in range(row + 1):
        if col == 0:
            result[row][col] = result[row - 1][col] + triangle[row][col]
        elif col == row:
            result[row][col] = result[row - 1][col - 1] + triangle[row][col]
        else:
            left = result[row - 1][col - 1]
            right = result[row - 1][col]
            result[row][col] = max(left, right) + triangle[row][col]

print(max(result[size - 1]))
