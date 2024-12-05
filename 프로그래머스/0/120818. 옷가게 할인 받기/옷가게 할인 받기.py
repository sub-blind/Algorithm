def solution(price):
    a = 0
    if price >=500000:
        a = int(price*0.8)
    elif price >= 300000:
        a = int(price*0.9)
    elif price >= 100000:
        a = int(price*0.95)
    else:
        a = price
    return a
    