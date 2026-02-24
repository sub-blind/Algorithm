def tree(left, right, depth):
    if left > right:
        return
    
    mid = (left + right) // 2
    result[depth].append(numbers[mid])
    
    tree(left, mid - 1, depth + 1)
    tree(mid + 1, right, depth + 1)


height = int(input())
numbers = list(map(int, input().split()))

result = [[] for _ in range(height)]

tree(0, len(numbers) - 1, 0)

for level in result:
    print(*level)