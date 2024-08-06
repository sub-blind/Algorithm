n = int(input())
for i in range(n):
    a = int(input())
    dictt= {}
    cnt = 1
    for j in range(a):
        wear = list(input().split())
        if wear[1] in dictt:
            dictt[wear[1]].append(wear[0])
        else:
            dictt[wear[1]] = [wear[0]]
    for k in dictt:
        cnt *= (len(dictt[k])+1)
    print(cnt-1)