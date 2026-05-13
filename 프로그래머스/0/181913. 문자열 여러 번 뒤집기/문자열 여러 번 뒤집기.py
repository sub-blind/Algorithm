def solution(my_string, queries):

    string_list = list(my_string)

    for s, e in queries:
        while s < e:
            string_list[s], string_list[e] = string_list[e], string_list[s]

            s += 1
            e -= 1

    return ''.join(string_list)