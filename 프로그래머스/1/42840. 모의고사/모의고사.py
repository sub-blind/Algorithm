def solution(answers):
    # 1번, 2번, 3번 수포자의 답안 패턴을 각각 정의
    pattern1 = [1, 2, 3, 4, 5]           # 1번 수포자: 5개 단위로 반복
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]  # 2번 수포자: 8개 단위로 반복
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 3번 수포자: 10개 단위로 반복

    # 패턴들을 리스트로 묶어 한 번에 관리
    patterns = [pattern1, pattern2, pattern3]

    # 수포자들의 점수를 저장할 리스트 초기화 (3명의 점수를 저장)
    scores = [0, 0, 0]

    # 정답 리스트(answers)를 순회하며 각 수포자의 점수를 계산
    for i, correct_answer in enumerate(answers):
        # i는 현재 정답의 인덱스, correct_answer는 정답 번호
        for student_index, pattern in enumerate(patterns):
            # 각 수포자의 답안 패턴에서 현재 문제에 해당하는 답 선택
            # 패턴은 반복되므로 `i % len(pattern)`으로 접근
            if correct_answer == pattern[i % len(pattern)]:
                # 정답일 경우, 해당 수포자의 점수 증가
                scores[student_index] += 1

    # 모든 수포자의 점수를 확인한 후, 가장 높은 점수(max_score)를 계산
    max_score = max(scores)

    # 최고 점수를 받은 수포자들의 번호를 리스트로 생성
    # enumerate(scores)는 (수포자 인덱스, 점수) 쌍을 반환
    result = []
    for student_index, score in enumerate(scores):
        if score == max_score:
            # 최고 점수를 받은 수포자는 1번부터 시작하므로 +1
            result.append(student_index + 1)

    return result
