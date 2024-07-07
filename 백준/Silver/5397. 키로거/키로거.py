a = int(input())
for _ in range(a):
    command = input().strip()
    left = []  
    right = []  

    for char in command:
        if char == "-":
            if left:
                left.pop()  
        elif char == "<":
            if left:
                right.append(left.pop())  
        elif char == ">":
            if right:
                left.append(right.pop()) 
        else:
            left.append(char)  

    left.extend(reversed(right))
    print("".join(left))
