def solution(intStrs, k, s, l):
    answer = []
    end = s + l
    for i in intStrs:
        sub_string = i[s:end]
        num = int(sub_string)
        if num > k:
            answer.append(num)
    return answer