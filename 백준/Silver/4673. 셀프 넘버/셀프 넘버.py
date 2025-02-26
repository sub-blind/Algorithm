def sol(n):
    x = list(str(n))
    sum = 0
    for i in range(len(x)):
        sum += int(x[i])
    sum = sum+n
    return sum

results = set()
for i in range(10000):
    results.add(sol(i))
for j in range(1,10001):
    if j not in results:
        print(j)