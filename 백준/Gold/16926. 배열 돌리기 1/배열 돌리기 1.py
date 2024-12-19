from sys import stdin

def main():
    from sys import stdin
    n, m, r = map(int, stdin.readline().split())
    matrix = [stdin.readline().split() for _ in range(n)]
    answer = [[0] * m for _ in range(n)]
    loops = min(n, m) // 2

    for i in range(loops):
        layer = []
        layer += matrix[i][i:m-i]
        layer += [matrix[y][m-i-1] for y in range(i+1, n-i-1)]
        layer += matrix[n-i-1][i:m-i][::-1]
        layer += [matrix[y][i] for y in range(n-i-2, i, -1)]

        l = len(layer)
        r_eff = r % l
        rotated = layer[r_eff:] + layer[:r_eff]

        idx = 0
        for j in range(i, m-i):
            answer[i][j] = rotated[idx]
            idx += 1
        for y in range(i+1, n-i-1):
            answer[y][m-i-1] = rotated[idx]
            idx += 1
        for j in range(m-i-1, i-1, -1):
            answer[n-i-1][j] = rotated[idx]
            idx += 1
        for y in range(n-i-2, i, -1):
            answer[y][i] = rotated[idx]
            idx += 1

    for row in answer:
        print(" ".join(row))

if __name__ == "__main__":
    main()
