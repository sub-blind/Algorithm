dic = {}
for i in range(int(input())) :
    name, lev = input().split()
    dic[int(lev)] = name
print(dic[min(dic.keys())])