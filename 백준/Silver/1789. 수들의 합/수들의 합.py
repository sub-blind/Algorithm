a = int(input())
b = 0
c = 0
while 1:
    c += 1
    b += c
    if b > a:
        break
print(c-1)