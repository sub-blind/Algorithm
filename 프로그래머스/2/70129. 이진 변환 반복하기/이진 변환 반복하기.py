def solution(s):
    count = 0 
    zero = 0

    while s != '1':
        zeros = s.count('0')
        zero += zeros
        s = bin(len(s) - zeros)[2:]
        count += 1

    return [count, zero]
