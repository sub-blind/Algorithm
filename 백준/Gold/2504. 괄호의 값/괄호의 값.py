p = list(input().strip())  # 입력 문자열을 리스트로 변환
stack = []  # 괄호의 짝을 확인하기 위한 스택
res = 1  # 현재 괄호의 값을 계산하기 위한 변수
result = 0  # 최종 결과를 저장할 변수

for i in range(len(p)):
    if p[i] == '(':
        res *= 2  # '('를 만나면 현재 값을 2배로
        stack.append(p[i])  # 스택에 '(' 추가
    elif p[i] == '[':
        res *= 3  # '['를 만나면 현재 값을 3배로
        stack.append(p[i])  # 스택에 '[' 추가
    elif p[i] == ')':
        if not stack or stack[-1] != '(':
            result = 0  # 스택이 비었거나 짝이 맞지 않으면 잘못된 구조
            break
        if p[i - 1] == '(':
            result += res  # 직전 괄호가 '('이면 현재 값을 결과에 추가
        res //= 2  # ')'를 만나면 현재 값을 2로 나눔
        stack.pop()  # 스택에서 '('를 제거
    elif p[i] == ']':
        if not stack or stack[-1] != '[':
            result = 0  # 스택이 비었거나 짝이 맞지 않으면 잘못된 구조
            break
        if p[i - 1] == '[':
            result += res  # 직전 괄호가 '['이면 현재 값을 결과에 추가
        res //= 3  # ']'를 만나면 현재 값을 3으로 나눔
        stack.pop()  # 스택에서 '['를 제거

# 최종적으로 스택이 비어있지 않으면 잘못된 괄호 구조
if stack:
    print(0)
else:
    print(result)  # 올바른 경우 결과 출력
