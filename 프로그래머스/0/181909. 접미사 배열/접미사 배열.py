def solution(my_string):
    answer = []

    for i in range(len(my_string)):
        a = my_string[i:]
        answer.append(a)

    answer.sort()

    return answer