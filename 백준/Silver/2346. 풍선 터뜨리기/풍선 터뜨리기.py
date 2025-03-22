from collections import deque

n = int(input())  # 사람 수 입력
turns = list(map(int, input().split()))  # 각 사람의 이동 수 입력
deq = deque([(i + 1, turns[i]) for i in range(n)])  # (사람 번호, 이동 수) 튜플로 저장
answer = []

while deq:
    idx, now_turn = deq.popleft()  # 사람 번호와 이동 수
    answer.append(idx)  # 사람 번호를 결과에 추가
    
    # 이제 해당 사람의 이동 수에 맞게 큐를 회전
    if now_turn > 0:
        deq.rotate(-(now_turn - 1))  # 양의 수일 때는 왼쪽으로 회전
    elif now_turn < 0:
        deq.rotate(-now_turn)  # 음의 수일 때는 오른쪽으로 회전

print(' '.join(map(str, answer)))  # 결과 출력
