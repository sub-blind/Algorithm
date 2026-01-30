def solution(progresses, speeds):
    result = []
    index = 0

    while index < len(progresses):
        days = 0
        while progresses[index] + days * speeds[index] < 100:
            days += 1

        count = 0
        while index < len(progresses) and progresses[index] + days * speeds[index] >= 100:
            count += 1
            index += 1

        result.append(count)

    return result
