s = input()
answer = []

for i in s:
    if 'a' <= i <= 'z':  
        answer.append(chr(((ord(i) - ord('a') + 13) % 26) + ord('a')))
    elif 'A' <= i <= 'Z':  
        answer.append(chr(((ord(i) - ord('A') + 13) % 26) + ord('A')))
    else:
        answer.append(i)  

print(''.join(answer))