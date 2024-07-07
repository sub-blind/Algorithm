a = input()
b = input()
cnt = 0

for i in range(97, 123):  # 소문자 a부터 z까지
    cnt += abs(a.count(chr(i)) - b.count(chr(i)))

print(cnt)
