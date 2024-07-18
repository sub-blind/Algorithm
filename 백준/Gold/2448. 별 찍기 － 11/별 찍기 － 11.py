import sys

input = sys.stdin.readline

n = int(input())

star = ["  *  ", " * * ", "*****"]

while len(star) < n:
    length = len(star)
    new_star = []

    for row in star:
        new_star.append(" " * length + row + " " * length)

    for row in star:
        new_star.append(row + " " + row)

    star = new_star

for row in star:
    print(row)
