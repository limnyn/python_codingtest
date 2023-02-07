# 서로 다른 정수를 입력받아 가능한 모든 순열을 리턴하라

nums = [1,2,3]
# def permute(nums: list[int]) -> list[list[int]]:
#     results = []
#     prev_elements = []

#     def dfs(elements):
#         # 리프 노드일 때 결과 추가
#         if len(elements) == 0:
#             results.append(prev_elements[:])

#         # 순열 생성 재귀 호출
#         for e in elements:
#             next_elements = elements[:]
#             next_elements.remove(e)
#             prev_elements.append(e)
#             dfs(next_elements)
#             prev_elements.pop()
#     dfs(nums)
#     return results

# print(permute(nums))


# Itertools를 사용
import itertools
def permute(nums):
    return list(map(list, itertools.permutations(nums)))
print(permute(nums))