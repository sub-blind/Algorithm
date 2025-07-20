H = int(input())

for i in range(H):
    if i <= H // 2:
        stars = 2 * i + 1
    else:
        stars = 2 * (H - i - 1) + 1

    spaces = 2 * (H - stars)

    print('*' * stars + ' ' * spaces + '*' * stars)
