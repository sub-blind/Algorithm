s = input()
t = input()

stack = [t]

while stack:
    a = stack.pop()
    
    if len(a) == len(s):
        if a == s:
            print(1)
            exit()
        continue
    
    if a[-1] == "A":
        stack.append(a[:-1])
    
    if a[0] == "B":
        stack.append(a[::-1][:-1])

print(0)
