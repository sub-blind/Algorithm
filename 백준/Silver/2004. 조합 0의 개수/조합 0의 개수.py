N, M = map(int, input().split())

def count_factors_of_k(n, k):
    count = 0
    i = k
    while i <= n:
        count += n // i
        i *= k
    return count

five_count = count_factors_of_k(N, 5) - count_factors_of_k(M, 5) - count_factors_of_k(N - M, 5)
two_count = count_factors_of_k(N, 2) - count_factors_of_k(M, 2) - count_factors_of_k(N - M, 2)

answer = min(five_count, two_count)
print(answer)
