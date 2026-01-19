c = [500,100,50,10,5,1]
count =0

b = 1000 - int(input())
for a in c:
    count += b//a
    b = b%a
print(count)