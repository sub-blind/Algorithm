dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
ret = sum(dial.index(i) + 3 for char in a for i in dial if char in i)
print(ret)
