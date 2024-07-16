from collections import deque
import sys

input = sys.stdin.readline
test = int(input())

for _ in range(test):
    p = input().strip()
    n = int(input())
    arr = input().strip()[1:-1] #괄호 제거

    if arr:
        queue = deque(arr.split(","))
    else:
        queue = deque()

    flag = 0
    error = False

    for cmd in p:
        if cmd == "R":
            flag += 1
        elif cmd == "D":
            if not queue:
                print("error")
                error = True
                break
            if flag % 2 == 0: #짝수인지 확인 배열이 뒤집힌건지 그대로인지
                queue.popleft()
            else:
                queue.pop()

    if not error:
        if flag % 2 == 1:  # 짝수인지 확인 배열이 뒤집힌건지 그대로인지
            queue.reverse()

        print("[" + ",".join(queue) + "]")
