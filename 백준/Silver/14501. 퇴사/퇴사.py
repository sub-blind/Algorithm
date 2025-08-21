# 상담 개수 입력 받기
n = int(input())

# 각 상담에 걸리는 기간과 받을 수 있는 금액을 담은 리스트 만들기
consultations = [list(map(int, input().split())) for _ in range(n)]

# 각 날짜별 최대 수익을 저장할 dp 리스트 (하루씩 뒤로 계산)
max_profit = [0] * (n + 1)

# 뒤에서부터 앞으로 계산 (마지막 상담부터 시작)
for day in range(n - 1, -1, -1):
    duration = consultations[day][0]  # 상담 기간
    payment = consultations[day][1]   # 상담 보수

    # 상담이 기간 안에 끝나지 않으면, 그 상담을 못 하므로 이전 최대 이익 그대로 사용
    if day + duration > n:
        max_profit[day] = max_profit[day + 1]
    else:
        # 상담을 할지 말지 선택
        # 1. 상담 안 할 때: 다음 날부터의 최대 수익
        # 2. 상담 할 때: 상담 기간이 지난 후부터의 최대 수익 + 현재 상담 보수
        max_profit[day] = max(max_profit[day + 1], max_profit[day + duration] + payment)

# 0일째부터 시작하는 최대 수익 출력
print(max_profit[0])
