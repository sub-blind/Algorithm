def solution(numbers):
    numbers.sort()
    numbers = numbers[-1]*numbers[-2]
    return numbers