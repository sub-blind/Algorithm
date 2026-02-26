N = int(input())
nums = [int(x) for x in input().split()]
add, sub, mul, div = map(int, input().split())

max_value = -int(1e9)
min_value = int(1e9)

def dfs(curr, data, add, sub, mul, div):
    global max_value, min_value

    if curr == N:
        max_value = max(max_value, data)
        min_value = min(min_value, data)
        return

    if add > 0:
        dfs(curr + 1, data + nums[curr], add - 1, sub, mul, div)

    if sub > 0:
        dfs(curr + 1, data - nums[curr], add, sub - 1, mul, div)

    if mul > 0:
        dfs(curr + 1, data * nums[curr], add, sub, mul - 1, div)

    if div > 0:
        dfs(curr + 1, int(data / nums[curr]), add, sub, mul, div - 1)

dfs(1, nums[0], add, sub, mul, div)

print(max_value)
print(min_value)