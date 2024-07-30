while True:
    n = input().strip()
    if n == "0":
        break
    length = len(n)
    half = True
    for i in range(length // 2):
        if n[i] != n[length - i - 1]:
            half = False
            break
    if half:
        print("yes")
    else:
        print("no")
