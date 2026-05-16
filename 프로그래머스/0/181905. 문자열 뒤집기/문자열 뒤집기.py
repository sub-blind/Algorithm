def solution(my_string, s, e):
    a = list(my_string[s:e+1])
    a.reverse()
    a = "".join(a)
    answer = my_string[:s] + a + my_string[e+1:]
    return answer