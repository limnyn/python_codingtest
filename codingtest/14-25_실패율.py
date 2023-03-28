# https://school.programmers.co.kr/learn/courses/30/lessons/60063

# 실패율 = 스테이지에 도달했으나 아직 클리어 하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

N = 4
stages =	[4,4,4,4,4]

    
    
    
    
    
# result = [3,4,2,1,5]
# 1 2 2 2 3 3 4 6
# 1/12223346 1/8
# 222/2223346 3/7
# 33/3346     1/2
# 4/46        1/2



def solution(N, stages):
    # 전체 스테이지 N, 사용자 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages
    # 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하라
    
    from collections import Counter
    counter = Counter(stages)
    cnt = []
    for i in range(N+2):
        cnt.append(counter[i])


    result = []
    for i in range(1,N+1):  
        if cnt[i] == 0:
            result.append((i, 0))
        else:
            result.append((i, cnt[i] / sum(cnt[i:])))
        
    result.sort(key=lambda x : -x[1])
    result = [i[0] for i in result]



    return result





print(solution(N, stages))