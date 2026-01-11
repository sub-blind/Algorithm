case = int(input())
answer = 0

for _ in range(case):
    dice = list(map(int, input().split()))
    unique = set(dice)

    if len(unique) == 1:  # 모두 같음
        prize = 10000 + dice[0] * 1000
    elif len(unique) == 2:  # 두 개만 같음
        for d in unique:
            if dice.count(d) == 2:
                prize = 1000 + d * 100
                break
    else:  # 모두 다름
        prize = max(dice) * 100

    answer = max(answer, prize)

print(answer)
