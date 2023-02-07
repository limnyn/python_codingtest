# 모든 부분 집합을 리턴하라
nums = [1,2,3]

# dfs와 트리를 사용한 부분집합 리턴
result = []
def dfs(index, path):    
    # 매번 결과 추가
    result.append(path)
    # 경로를 만들면서 DFS
    for i in range(index, len(nums)):
        dfs(i+1, path+ [nums[i]])
dfs(0,[])
print(sorted(result,key=len))



# itertools와 combinations를 사용한 부분집합 리턴
# import itertools
# result = []
# for i in range(0, len(nums)+1):
#     line = (list(map(list, itertools.combinations(nums,i))))
#     for l in line:
#         result.append(l)
# print(sorted(result,reverse=True, key=len))

