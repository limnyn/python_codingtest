# 상현이는 디지털 시계를 하나 구매하였다. 상현이의 시계는 아래와 같은 7-segment 방식으로 숫자를 나타낸다. 7-segment는 숫자 1을 BC, 숫자 2는 ABGED를 켠 상태이다.



# 나머지 숫자는 아래 그림을 참고하면 된다.



# 디지털시계가 배터리가 부족하여 몇 개의 segment가 불이 들어오지 않는다. 현재 디지털시계의 4자리 숫자에 대한 7-segment의 상태가 주어질 때, 디지털시계가 나타낼 수 있는 시간을 앞선 시간부터 모두 출력한다. 불가능한 경우는 없다.

# 시계는 23:59에서 1분이 지나면 00:00으로 돌아온다.

# 입력
# S(sa, sb, sc, ... , sg): 4 자리 숫자에 대한 7-segment의 a부터 g까지 상태를 의미하며 1은 켜진 상태를 의미하고 0은 꺼진 상태를 의미한다.
# 00:00 부터 23:59 까지 유효한 시간에 대한 입력만 주어진다.
# 출력
# 현재 디지털 시계가 표현하는 가능한 모든 시간을 사전 순으로 반환한다
def compare_lists(A, B):
    for i in range(len(A)):
        if A[i] == 1 and B[i] == 0:
            return False
    return True

def solution(Parameter):
    answer = [[],[],[],[]]
    times =[ 
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
        for i in range(9):
            if compare_lists(para,times[i]):
                answer[index].append(i)
    print(answer)
    result = []    
    for i in answer[0]:
        for j in answer[1]:
            for k in answer[2]:
                for l in answer[3]:
                    hour = i * 10 + j
                    minute = k * 10 + l
                    if hour <= 23 and minute <= 59:
                        result.append([i, j, k, l])
    return result
# def compare_lists(A, B):
#     for i in range(len(A)):
#         if A[i] == 1 and B[i] == 0:
#             return False
#     return True

# def solution(Parameter):
#     answer = [[],[],[],[]]
#     times = [
#         [1,1,1,1,1,1,0], # 0
#         [0,1,1,0,0,0,0], # 1
#         [1,1,0,1,1,0,1], # 2
#         [1,1,1,1,0,0,1], # 3
#         [0,1,1,0,0,1,1], # 4
#         [1,0,1,1,0,1,1], # 5
#         [1,0,1,1,1,1,1], # 6
#         [1,1,1,0,0,0,0], # 7
#         [1,1,1,1,1,1,1], # 8
#         [1,1,1,1,0,1,1], # 9
#     ]
#     for index, para in enumerate(Parameter):
#         for i in range(9):
#             if compare_lists(para,times[i]):
#                 if index == 0 and i > 2 :
#                     break
            
#                 if index == 2 and i > 5:
#                     break
#                 answer[index].append(i)
#     result = []    
#     for i in answer[0]:
#         for j in answer[1]:
#             for k in answer[2]:
#                 for l in answer[3]:
#                     result.append([i, j, k, l])

#     return result
                


# S = [[1,0,0,1,0,0,1],[0,1,0,0,1,0,0],[0,0,0,0,0,1,1],[0,1,1,0,1,0,0]]
S = [[0,1,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,1,1],[0,1,1,0,1,0,0]]
print(solution(S))

# return = [[2,0,4,0],[2,0,4,8],[2,0,5,0],[2,0,5,8],[2,2,4,0],[2,2,4,8],[2,2,5,0],[2,2,5,8]]

# answer = [[],[],[],[]]
# print(answer)


