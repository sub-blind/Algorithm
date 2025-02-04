def solution(food):
    temp_list = []

    for i in range(1, len(food)):
        count = food[i] // 2
        temp_list.append(str(i) * count)

    left_side = ''.join(temp_list)
    result = left_side + '0' + left_side[::-1]
    return result
