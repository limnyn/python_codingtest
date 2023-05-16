# https://school.programmers.co.kr/learn/courses/30/lessons/181188


# [1,3,4,4,5,10,11]
# [4,7,5,8,12,14,13]

# [[1,4],[4,5],[3,7],[4,8],[5,12],[11,13],[10,14]]
# 4 < 4 
# [1,4]
# 5 > 3
# [[4,5],[3,7]]
# 5 > 4
# [[4,5],[3,7],[4,8]]

# 12 > 11
# [[5,12],[11,13]]
# 12 > 10
# [[5,12],[11,13],[10, 14]]


# [[1,4],[4,5],[3,7],[4,8],[5,12],[11,13],[10,14]]

def solution(targets):
    answer = 0
    targets.sort(key =lambda x:x[1])
    end = targets[0][1]
    
    idx = 1
    while(idx != len(targets)):
        # print(start, end, targets[idx], "index : ",idx, "answer : ",answer)
        
        if end <= targets[idx][0]:
            answer += 1
            end = targets[idx][1]

        idx += 1
        

    return answer + 1

        
            



    
