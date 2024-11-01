print("n e")
print("- -----------")

sum = 0.0
factorial = 1

for i in range(10):
    if i > 0:
        factorial *= i
    
    sum += 1 / factorial

    if i < 2:
        print(f"{i} {int(sum)}")
    elif i == 2:
        print(f"{i} {round(sum, 9)}")
    else:
        print(f"{i} {sum:.9f}")
