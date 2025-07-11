from datetime import date, timedelta

A, B, C = map(int, input().split())
end_date = date(A, B, C)
count = 1

seasons = [(3, 1), (6, 1), (9, 1), (12, 1)]

year = 2015
while True:
    for m, d in seasons:
        cur = date(year, m, d)
        if cur <= end_date:
            count += 1
        else:
            print(count)
            exit()
    year += 1
