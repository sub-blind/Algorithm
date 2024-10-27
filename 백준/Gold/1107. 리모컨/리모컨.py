def can_press(num_str, broken_buttons):
    for ch in num_str:
        if int(ch) in broken_buttons:
            return False
    return True

n = int(input())
m = int(input())

if m == 0:
    broken_buttons = set()
else:
    broken_buttons = set(map(int, input().split()))

minimum = abs(100 - n)
for i in range(1000001):
    num_str = str(i)
    if can_press(num_str, broken_buttons):
        minimum = min(minimum, abs(n - i) + len(num_str))

print(minimum)
