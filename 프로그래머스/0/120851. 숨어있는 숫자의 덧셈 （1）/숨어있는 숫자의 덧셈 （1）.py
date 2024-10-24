def solution(my_string):
    result = 0
    for i in my_string:
        if i.isdigit():
            result += int(i)
    return result

import re

def solution(my_string):
    return sum(map(int, re.findall(r'[0-9]', my_string)))