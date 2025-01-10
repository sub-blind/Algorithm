N = int(input())
cnt = N

for _ in range(N):
    word = input()
    seen = set()
    prev = ''
    for char in word:
        if char != prev:
            if char in seen:
                cnt -= 1
                break
            seen.add(char)
        prev = char

print(cnt)
