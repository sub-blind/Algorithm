import sys
input = sys.stdin.readline

n = int(input().strip())
n_arr = list(map(int, input().strip().split()))
m = int(input().strip())
m_arr = list(map(int, input().strip().split()))

n_arr.sort()

for target in m_arr:
    first = 0
    end = n - 1
    found = False

    while first <= end:
        mid = (first + end) // 2
        if n_arr[mid] == target:
            found = True
            break
        elif target < n_arr[mid]:
            end = mid - 1
        else:
            first = mid + 1

    if found:
        print(1)
    else:
        print(0)
