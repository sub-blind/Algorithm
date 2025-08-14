N = int(input())
pizza_list = list(map(int, input().split()))
time_list = [0] * N
steps = 0
index = 0

while any(pizza_list):
    if pizza_list[index] > 0:
        pizza_list[index] -= 1
        steps += 1
        if pizza_list[index] == 0 and time_list[index] == 0:
            time_list[index] = steps
    index = (index + 1) % N

print(*time_list)