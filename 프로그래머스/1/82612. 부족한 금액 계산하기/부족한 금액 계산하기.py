def solution(price, money, count):
    total_cost = 0
    for i in range(1, count + 1):
        total_cost += price * i
    if money < total_cost:
        return total_cost - money
    else:
        return 0
