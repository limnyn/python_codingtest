# https://school.programmers.co.kr/learn/courses/30/lessons/87946

def solution(k, dungeons):
    """
    [조건]
        던전의 갯수는 8개 이하
        
    [최대한 많은 던전 탐험]
        현재 상황에서 방문하지 않은 가능한 던전 확인 후 탐험
        이후 탐험할 수 있는 던전이 없으면 이때까지 탐험한 던전 갯수 갱신
    """
    answer = 0
    visited = [False] * len(dungeons)
    
    def dfs(visited, fatigability, num_of_visit):
        nonlocal answer

        for i in range(len(dungeons)):
            if not visited[i] and fatigability >= dungeons[i][0]:
                visited[i] = True
                dfs(visited, fatigability - dungeons[i][1], num_of_visit + 1)
                visited[i] = False
        
        
        answer = max(answer, num_of_visit)
    dfs(visited, k, 0)       
    return answer

# print(solution(80,[[80,20],[50,40],[30,10]]))