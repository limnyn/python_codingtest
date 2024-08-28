# https://school.programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):
    check_dict = {}
    for runner in participant:
        if check_dict.get(runner):
            check_dict[runner] += 1
        else:
            check_dict[runner] = 1
    for runner in completion:
        check_dict[runner] -= 1
    
    for i, v in check_dict.items():
        if v != 0:
            return i
    
    
    