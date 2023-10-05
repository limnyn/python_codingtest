# https://school.programmers.co.kr/learn/courses/30/lessons/12947
def solution(x):
    #     line = list(str(x))
    #     num_sum = 0
    #     for num in line:
    #         num_sum += int(num)
    #     if x % num_sum == 0:
    #         return True
    #     return False

    return x % sum(int(i) for i in str(x)) == 0
