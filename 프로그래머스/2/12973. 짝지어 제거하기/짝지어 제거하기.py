def solution(s):
    box = []
    
    for letter in s:
        if box and box[-1] == letter:
            box.pop()
        else:
            box.append(letter)
    
    if box:
        return 0
    else:
        return 1
