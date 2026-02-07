a, b, c = map(int, input().split())
d = input()

a, b, c = sorted((a, b, c))

for i in d:
    if i == 'A':
        print(a, end=' ')
    elif i == 'B':
        print(b, end=' ')
    else:
        print(c, end=' ')