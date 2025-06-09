a = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
b = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m, d = map(int, input().split())
day = sum(b[:m-1]) + d
print(a[day % 7])