n = int(input())
num = 666
cnt = 0
while 1:
    if '666' in str(num):
        cnt += 1
    if cnt == n:
        break
    num += 1
print(num)