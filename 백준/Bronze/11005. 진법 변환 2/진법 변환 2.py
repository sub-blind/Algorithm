a, b = map(int, input().split())
num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = []

while a > 0:
    result.append(num_list[a % b])
    a //= b
print(''.join(reversed(result)) if result else "0")
