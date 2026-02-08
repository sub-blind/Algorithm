from collections import Counter

def solution(clothes):
    answer = 1

    categories = []
    for name, category in clothes:
        categories.append(category)

    cnt = Counter(categories)

    for count in cnt.values():
        answer *= (count + 1)

    return answer - 1
