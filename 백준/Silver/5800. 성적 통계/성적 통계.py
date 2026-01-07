T = int(input())  # 테스트 케이스 개수

for class_number in range(1, T + 1):
    data = list(map(int, input().split()))
    
    student_count = data[0]         
    scores = sorted(data[1:])      

    minimum_score = scores[0]       
    maximum_score = scores[-1]       

    largest_gap = 0
    for i in range(student_count - 1):
        gap = scores[i + 1] - scores[i]
        if gap > largest_gap:
            largest_gap = gap

    print(f"Class {class_number}")
    print(f"Max {maximum_score}, Min {minimum_score}, Largest gap {largest_gap}")
