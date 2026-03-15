alphabet_count = [0 for i in range(26)]

while True:
    try:
        text = input()  
        
        for char in text:
            if char.islower():
                index = ord(char) - ord('a')
                alphabet_count[index] += 1

    except EOFError:
        break

max_count = max(alphabet_count)

for i in range(26):
    if alphabet_count[i] == max_count:
        print(chr(i + ord('a')), end='')