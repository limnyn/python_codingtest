# def compare_lists(A, B):
#     for i in range(len(A)):
#         if A[i] == 1 and B[i] == 0:
#             return False
#     return True

# def solution(Parameter):
#     result = [[], [], [], []]
#     times = [
#         [1, 1, 1, 1, 1, 1, 0], # 0
#         [0, 1, 1, 0, 0, 0, 0], # 1
#         [1, 1, 0, 1, 1, 0, 1], # 2
#         [1, 1, 1, 1, 0, 0, 1], # 3
#         [0, 1, 1, 0, 0, 1, 1], # 4
#         [1, 0, 1, 1, 0, 1, 1], # 5
#         [1, 0, 1, 1, 1, 1, 1], # 6
#         [1, 1, 1, 0, 0, 0, 0], # 7
#         [1, 1, 1, 1, 1, 1, 1], # 8
#         [1, 1, 1, 1, 0, 1, 1], # 9
#     ]
#     for index, para in enumerate(Parameter):
#         for i in range(len(times)):
#             if compare_lists(para, times[i]):
#                 result[index].append(i)
#     # print(result)
#     answer = []    
#     for i in result[0]:
#         for j in result[1]:
#             for k in result[2]:
#                 for l in result[3]:
#                     hour = i * 10 + j
#                     minute = k * 10 + l
#                     if hour <= 23 and minute <= 59:
#                         answer.append([i, j, k, l])
#     return answer

def compare_lists(A, B):
    for i in range(len(A)):
        if A[i] == 1 and B[i] == 0:
            return False
    return True

def solution(Parameter):
    result = [[], [], [], []]
    times = [
        [1, 1, 1, 1, 1, 1, 0], # 0
        [0, 1, 1, 0, 0, 0, 0], # 1
        [1, 1, 0, 1, 1, 0, 1], # 2
        [1, 1, 1, 1, 0, 0, 1], # 3
        [0, 1, 1, 0, 0, 1, 1], # 4
        [1, 0, 1, 1, 0, 1, 1], # 5
        [1, 0, 1, 1, 1, 1, 1], # 6
        [1, 1, 1, 0, 0, 0, 0], # 7
        [1, 1, 1, 1, 1, 1, 1], # 8
        [1, 1, 1, 1, 0, 1, 1], # 9
    ]
    for index, para in enumerate(Parameter):
        for i in range(len(times)):
            if compare_lists(para, times[i]):
                result[index].append(i)

    answer = []    
    for i in result[0]:
        for j in result[1]:
            for k in result[2]:
                for l in result[3]:
                    hour = i * 10 + j
                    minute = k * 10 + l
                    if hour <= 23 and minute <= 59:
                        answer.append([i, j, k, l])
    return sorted(answer)

S = [[1,1,1,1,1,1,0],[0,1,0,0,1,0,0],[0,0,0,0,0,1,1],[0,1,1,1,1,1,0]]
ex = [[2,0,4,0],[2,0,4,8],[2,0,5,0],[2,0,5,8],[2,2,4,0],[2,2,4,8],[2,2,5,0],[2,2,5,8]]
print(solution(S))