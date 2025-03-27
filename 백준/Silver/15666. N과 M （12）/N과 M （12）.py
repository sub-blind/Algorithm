# 백트래킹 함수
def generate_combinations(start_idx, current_combination):
    # 수열의 길이가 m이 되면 현재 수열을 출력
    if len(current_combination) == m:
        print(*current_combination)
        return

    # start_idx부터 시작해서 배열의 끝까지 탐색
    for i in range(start_idx, len(unique_numbers)):
        # 현재 숫자를 선택한 후 재귀적으로 호출
        generate_combinations(i, current_combination + [unique_numbers[i]])

# 입력 처리
n, m = map(int, input().split())  # n: 숫자의 개수, m: 수열의 길이
numbers = list(map(int, input().split()))  # 숫자 배열

# 중복을 제거하고 정렬한 후 unique_numbers에 저장
unique_numbers = sorted(set(numbers))

# 백트래킹 함수 호출, 초기값(start_idx=0, current_combination=빈 리스트)
generate_combinations(0, [])
