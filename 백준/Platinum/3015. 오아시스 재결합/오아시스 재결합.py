import sys
input = sys.stdin.readline

num = int(input()) 

stack = [] 
cnt = 0

for _ in range(num):

    person = int(input())

    if not stack or person < stack[-1][0]:
        stack.append([person, 1])

    elif person == stack[-1][0] :
        cnt += stack[-1][1]
        stack[-1][1] += 1

    else: 

        while stack and person > stack[-1][0]: 
            cnt += stack.pop()[-1]

        if stack and person == stack[-1][0]:
            cnt += stack[-1][1]
            stack[-1][1] += 1

        else:
            stack.append([person, 1])

    if len(stack) > 1:
        cnt += 1

print(cnt)