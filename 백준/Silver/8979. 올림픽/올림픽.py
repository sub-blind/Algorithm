a=[]
n,k=map(int,input().split())
for p in range(n):
    a.append(list(map(int,input().split())))
a.sort(key=lambda x:(-x[1],-x[2],-x[3]))
for j in range(n):
    if a[j][0]==k:
        index=j
for i in range(n):
    if a[i][1:]== a[index][1:]:
        print(i+1)
        break