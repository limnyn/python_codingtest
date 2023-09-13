# https://school.programmers.co.kr/learn/courses/30/lessons/120869

from collections import Counter


def solution(spell, dic):
    answer = 0
    dics = []
    for word in dic:
        dics.append(Counter(word))

    for counter in dics:
        result = 0
        for char in spell:
            if counter[char] == 1:
                result += 1

        if result == len(spell):
            return 1
    return 2
