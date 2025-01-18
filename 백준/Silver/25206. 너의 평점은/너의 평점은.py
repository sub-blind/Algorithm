total_weighted_score = 0
total_credits = 0

grade_to_gpa = {
    "A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, 
    "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0
}

for _ in range(20):
    subject_name, credit, grade = input().split()
    if grade == "P":
        continue
    total_weighted_score += float(credit) * grade_to_gpa[grade]
    total_credits += float(credit)

gpa = total_weighted_score / total_credits
print(gpa)
