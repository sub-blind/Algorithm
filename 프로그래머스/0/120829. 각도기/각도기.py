def solution(angle):
    if angle < 90:
        a= 1
    elif angle == 90:
        a=2
    elif 90 < angle <180:
        a=3
    else:
        a=4
    return a