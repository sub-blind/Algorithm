def solution(myString):
    split_result = myString.split("x")

    answer = []

    for s in split_result:
        length = len(s)
        answer.append(length)

    return answer