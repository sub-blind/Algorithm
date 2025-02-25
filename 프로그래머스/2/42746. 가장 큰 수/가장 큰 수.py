def solution(numbers):
    numbers = list(map(str, numbers))

    def compare(x):
        return x * 10
    
    numbers.sort(key=compare, reverse=True)
    
    answer = ''.join(numbers)

    if answer[0] == '0':
        return '0'
    
    return answer
