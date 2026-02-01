s = 0
cnt = [0] * (1000000 + 1)

for _ in range(10):
    a = int(input())
    s += a  
    cnt[a] += 1

print(s // 10)  # 최대값
print(cnt.index(max(cnt)))