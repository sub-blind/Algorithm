n = int(input())
m = int(input())
lights = list(map(int, input().split()))

heights = max(lights[0], (lights[0] + 1) // 2)

for i in range(1, m):
    distance = (lights[i] - lights[i - 1] + 1) // 2
    heights = max(heights, distance)

heights = max(heights, n - lights[-1])

print(heights)
