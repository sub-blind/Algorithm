N = int(input())
arr = []
for _ in range(N):
    a = int(input()) #높이
    arr.append(a)
cnt = 0
stack = []
for i in range(N):
    while stack:
        if arr[i] >= stack[-1]:
            stack.pop()
        else:
            cnt += len(stack)
            break
    stack.append(arr[i])
print(cnt)