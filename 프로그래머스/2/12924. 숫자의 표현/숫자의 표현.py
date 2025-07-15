def solution(n):
    count = 0
    for start in range(1, n + 1):
        total = start
        next_num = start + 1
        while total < n:
            total += next_num
            next_num += 1
        if total == n:
            count += 1
    return count
