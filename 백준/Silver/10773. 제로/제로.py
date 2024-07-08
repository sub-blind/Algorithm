import sys 
n = int(sys.stdin.readline())
stack =[]

for i in range(n):
    command = int(sys.stdin.readline())
    if command != 0:
        stack.append(command)
    else:
        stack.pop()
        
print(sum(stack))