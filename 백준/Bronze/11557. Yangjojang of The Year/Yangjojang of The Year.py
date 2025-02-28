case = int(input())

for i in range(case):
    school = []
    drink = []
    n = int(input())
    for j in range(n):
        a, b = input().split()
        school.append(a)
        drink.append(int(b))
    idx = drink.index(max(drink))
    print(school[idx])