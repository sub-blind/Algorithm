def solution(left, right):
    answer = 0

    for i in range(left, right + 1):
        # 약수의 개수를 판단하기 위해 제곱근 사용
        if int(i ** 0.5) ** 2 == i:
            answer -= i  # 제곱수는 약수의 개수가 홀수
        else:
            answer += i  # 그 외는 약수의 개수가 짝수

    return answer
