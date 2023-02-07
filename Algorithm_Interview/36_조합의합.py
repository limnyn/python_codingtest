# 숫자 집합 candidates를 조합하여 합이 target이 되는 원소를 나열하라. 
# 각 원소는 중복으로 낭려 가능하다.


candidates = [2,3,6,7]
target = 7

def combinationSum(candidates, target):
    result = []
    
    def dfs(csum, index, path):
        # 종료 조건
        if csum < 0:
            return
        if csum == 0:
            result.append(path)
            return
        
        # 자신 부터 하위 원소 까지의 나열 재귀 호출
        for i in range(index, len(candidates)):
            dfs(csum - candidates[i], i, path + [candidates[i]])

    dfs(target, 0, [])
    return result

print(combinationSum(candidates,target))