
A, P = map(int, input().split())

axel_income = A * 7
petra_income = P * 13

if axel_income > petra_income:
    print("Axel")
elif axel_income < petra_income:
    print("Petra")
else:
    print("lika")
