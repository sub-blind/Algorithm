n = int(input())
people=[]
for _ in range(n):
    a,b = input().rstrip().split()
    if b == 'enter':
        people.append(a)
    else:
        people.remove(a)

people.sort(reverse=True)
print("\n".join(people))