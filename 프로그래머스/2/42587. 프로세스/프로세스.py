from collections import deque

def solution(priorities, location):
    q = deque(priorities)
    answer = 0

    while True:
        if q[0] < max(q):
            q.append(q.popleft())
        else:
            answer += 1
            q.popleft()
            if location == 0:
                return answer

        if location == 0:
            location = len(q) - 1
        else:
            location -= 1