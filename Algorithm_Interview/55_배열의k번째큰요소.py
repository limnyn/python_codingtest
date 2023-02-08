# 정렬되지 않은 배열에서 k번째 큰 요소를 추출하라
import heapq
nums = list(map(int, input().split()))
k = int(input())

heap = list()
for n in nums:
    heapq.heappush(heap, -n)

# # 힙으로 추출
# for i in range(0,k-1):
#     heapq.heappop(heap)
# print(-heapq.heappop(heap))


# nlargest(k, nums)는 가장 큰수 k개의 리스트를 반환하고, 그 마지막 index가 정답이다
# print(heapq.nlargest(k, nums)[-1])

# 팀소트 내장함수를 사용하면 가장 빠르게 풀 수 있다.
print(sorted(nums, reverse=True)[k-1])