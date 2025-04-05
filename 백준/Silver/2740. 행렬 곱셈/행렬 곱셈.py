# 첫 번째 행렬 A의 크기 N x M을 입력받음
N, M = map(int, input().split())

# 첫 번째 행렬 A의 값을 입력받음
A = [list(map(int, input().split())) for _ in range(N)]

# 두 번째 행렬 B의 크기 M x K을 입력받음
M, K = map(int, input().split())

# 두 번째 행렬 B의 값을 입력받음
B = [list(map(int, input().split())) for _ in range(M)]

# 결과 행렬 AxB의 크기는 N x K 이므로, 그에 맞는 크기의 2D 리스트를 생성
AxB = [[0] * K for _ in range(N)]

# 두 행렬 A와 B를 곱해서 결과 행렬 AxB를 구하는 과정
for row in range(N):  # A의 각 행에 대해
    for col in range(K):  # B의 각 열에 대해
        result = 0  # 행렬 곱셈 결과를 저장할 변수
        for i in range(M):  # A의 각 열과 B의 각 행을 곱하고 더하기
            result += A[row][i] * B[i][col]
        AxB[row][col] = result  # 결과 행렬에 값을 저장

# 결과 행렬 AxB를 출력
for r in AxB:
    print(*r)  # 각 행을 출력할 때 공백으로 구분하여 출력
