from itertools import combinations

def solution(nums):
    answer = 0
    prime_nums = set()

    for a, b, c in combinations(nums, 3):
        s = a + b + c
        if s in prime_nums:
            answer += 1
            continue
        
        # 소수 판별
        is_prime = True
        for i in range(2, int(s ** 0.5) + 1):
            if s % i == 0:
                is_prime = False
                break
        
        if is_prime:
            prime_nums.add(s)
            answer += 1

    return answer
