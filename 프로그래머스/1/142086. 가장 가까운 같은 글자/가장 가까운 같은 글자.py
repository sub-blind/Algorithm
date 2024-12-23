def solution(s):
    answer = []
    word_dict = {}

    for idx, word in enumerate(s):
        if word in word_dict:
            answer.append(idx - word_dict[word])
        else:
            answer.append(-1)
        word_dict[word] = idx

    return answer