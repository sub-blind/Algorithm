num = input()
answer = ''
stack = []

# 연산자의 우선순위 설정
precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

for i in num:
    if i.isalpha():
        answer += i
    elif i == '(':
        stack.append(i)
    elif i == ')':
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.pop()  # '(' 제거
    else:  # +, -, *, /
        while (stack and stack[-1] != '(' and
               precedence.get(i, 0) <= precedence.get(stack[-1], 0)):
            answer += stack.pop()
        stack.append(i)

# 스택에 남은 연산자 처리
while stack:
    answer += stack.pop()

print(answer)
