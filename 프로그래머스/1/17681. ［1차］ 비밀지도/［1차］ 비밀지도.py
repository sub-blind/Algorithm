def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        combined = arr1[i] | arr2[i]
        binary = format(combined, 'b').zfill(n)
        
        temp = ''
        for ch in binary:
            if ch == '1':
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)
        
    return answer