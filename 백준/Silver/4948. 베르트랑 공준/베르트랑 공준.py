def sosu(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

all_list = list(range(2, 246912))
memo = [i for i in all_list if sosu(i)]

while True:
    n = int(input())
    if n == 0:
        break
    count = sum(1 for i in memo if n < i <= 2 * n)
    print(count)
