a = int(input())

res = 5*a - 400
print(res)

if res < 100:
    print(1)
elif res == 100:
    print(0)
else:
    print(-1)