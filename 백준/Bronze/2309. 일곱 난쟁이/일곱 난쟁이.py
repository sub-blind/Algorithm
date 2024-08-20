arr = []
for i in range(9):
    arr.append(int(input()))
arr.sort()
k = sum(arr)-100
for i in range(9):
    if sum(arr) == 100:
        break
    for x in range(i+1,9):
        if arr[i] + arr[x] == k:
            arr[i] = arr[x] = 0
            break
for i in arr:
    if i != 0:
        print(i)