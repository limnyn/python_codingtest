def solution(Parameter):
    answer = []
    
    for num in Parameter:
        if num == [0,1,1,0,0,0,0]:
            answer.append(1)
        elif num == [1,1,0,1,1,0,1]:
            answer.append(2)
        elif num == [1,1,1,1,0,0,1]:
            answer.append(3)
        elif num == [0,1,1,0,0,1,1]:
            answer.append(4)
        elif num == [1,0,1,1,0,1,1]:
            answer.append(5)
        elif num == [0,0,1,1,1,1,1]:
            answer.append(6)
        elif num == [1,1,1,0,0,0,0]:
            answer.append(7)
        elif num == [1,1,1,1,1,1,1]:
            answer.append(8)
        elif num == [1,1,1,1,0,1,1]:
            answer.append(9)
        elif num == [1,1,1,1,1,1,0]:
            answer.append(0)                                                                                              
    return answer


S = [[1,1,1,1,1,1,0],[1,1,1,1,1,1,0],[1,0,1,1,0,1,1],[1,0,1,1,0,1,1]]
print(solution(S))