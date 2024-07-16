while 1:
    a = input()
    arr = []
    if a == ".":
        break
    for i in a:
        if i == "[" or i == "(":
            arr.append(i)
            
        elif i == "]":
            if len(arr) != 0 and arr[-1] == "[":
                arr.pop()
            else:
                arr.append("]")
                break
            
        elif i == ")":
            if len(arr) != 0 and arr[-1] == "(":
                arr.pop()
            else:
                arr.append(")")
                break
            
    if len(arr) == 0:
        print("yes")
    else:
        print("no")
