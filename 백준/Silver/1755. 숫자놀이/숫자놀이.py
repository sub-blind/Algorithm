numstring = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}

n, m = map(int, input().split())

numbers = []

for i in range(n, m + 1):
    num_str = str(i)
    if len(num_str) > 1:
        word = [numstring[digit] for digit in num_str]
    else:
        word = [numstring[num_str[0]]]
    numbers.append(word)

numbers.sort()

result = []

for word_list in numbers:
    number_str = ''.join(str(list(numstring.values()).index(word)) for word in word_list)
    result.append(int(number_str))

for i in range(len(result)):
    if i % 10 == 0 and i != 0:
        print()
    print(result[i], end=" ")
