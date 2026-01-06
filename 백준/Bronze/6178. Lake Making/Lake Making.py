import sys

def solve():
    input = sys.stdin.read().split()
    if not input:
        return
    
    R = int(input[0])  # 행
    C = int(input[1])  # 열
    E = int(input[2])  # 수위
    N = int(input[3])  # 명령어 개수
    
    idx = 4
    grid = []
    for r in range(R):
        grid.append([int(x) for x in input[idx : idx + C]])
        idx += C
        
    for _ in range(N):
        rs = int(input[idx]) - 1
        cs = int(input[idx+1]) - 1
        ds = int(input[idx+2])
        idx += 3
        
        max_elev = 0
        for r in range(rs, rs + 3):
            for c in range(cs, cs + 3):
                if grid[r][c] > max_elev:
                    max_elev = grid[r][c]
        
        target_elev = max_elev - ds
        
        for r in range(rs, rs + 3):
            for c in range(cs, cs + 3):
                if grid[r][c] > target_elev:
                    grid[r][c] = target_elev

    total_depth = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] < E:
                total_depth += (E - grid[r][c])
    
    result = total_depth * 72 * 72
    print(result)

if __name__ == "__main__":
    solve()