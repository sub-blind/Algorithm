from collections import Counter

n = int(input())
data = list(map(int, input().split()))
count = Counter(data)  # 각 수의 빈도 계산
stack = []
result = [-1] * n  # 결과를 저장할 배열

for i in range(n):
    while stack and count[data[stack[-1]]] < count[data[i]]:
        result[stack.pop()] = data[i]
    stack.append(i)  # 현재 인덱스를 스택에 추가

for r in result:
    print(r, end=' ')
