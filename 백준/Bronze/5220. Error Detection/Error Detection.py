a = int(input())

for i in range(a):
    number, check_bit = map(int, input().split())

    binary_string = bin(number)[2:]
    count_of_ones = binary_string.count('1')

    if count_of_ones % 2 == check_bit:
        print("Valid")
    else:
        print("Corrupt")
