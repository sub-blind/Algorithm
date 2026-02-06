num = []
for _ in range(9):
    num.append(int(input()))

a = sum(num)

for i in range(9):
    for j in range(i+1, 9):

        if a-num[i]-num[j] == 100:

            for k in range(9):
                if k != i and k != j:
                    print(num[k])

            exit()
