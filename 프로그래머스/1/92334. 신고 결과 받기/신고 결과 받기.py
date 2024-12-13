from collections import defaultdict

def solution(id_list, report, k):
    # 중복 신고를 없애고, 신고를 유저별로 묶음
    report = set(report)
    
    # 신고를 받은 사람의 신고 횟수 계산
    report_count = defaultdict(int)  # 유저별 신고 횟수
    arrayReport = defaultdict(list)  # 유저별 신고한 사람 목록
    
    for entry in report:
        reporter, reported = entry.split()
        arrayReport[reporter].append(reported)
        report_count[reported] += 1
    
    reportK = {user for user, count in report_count.items() if count >= k}
    
    answer = []
    for user in id_list:
        count = sum(1 for reported in arrayReport[user] if reported in reportK)
        answer.append(count)
    
    return answer
