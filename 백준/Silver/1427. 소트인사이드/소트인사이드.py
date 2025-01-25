n=int(input())
lis=[]
n=str(n)
for i in n:
    lis.append(i)
    
lis.sort(reverse=True)
for i in lis:
    print(i,end="")