n = int(input())
r = list(map(int,input().split()))

for b in r[1:]:
    a = r[0]
    while(True):
        for i in range(2,min(a,b)+1):
            if a%i == 0 and b%i == 0:
                a//=i
                b//=i
                break
        else:
            print(a,"/",b,sep="")
            break