def recursion(s, l, r):
    checks = 1
    while l < r:
        if s[l] != s[r]:
            return 0, checks
        l = l + 1
        r = r - 1
        checks = checks + 1
    return 1, checks

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

t = int(input())
for i in range(t):
    s = input()
    answer = list(isPalindrome(s))
    print(answer[0], answer[1])