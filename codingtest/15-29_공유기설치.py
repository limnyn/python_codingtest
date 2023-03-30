# https://www.acmicpc.net/problem/2110
import bisect

# 파라메트릭서치 문제


n, c = map(int, input().split())
nums = []


for _ in range(n):
    nums.append(int(input()))
nums.sort() # 이진탐색 수행을 위해 정렬

start = 1 # 가능한 최소 거리(min-gap)
end = nums[-1] - nums[0]
result = 0

while(start <= end):
    mid = (start  + end) // 2 # mid는 가장 인접한 두 공유기 사이의 거리(gap)를 의미
    value  =nums[0]
    count = 1
    # 현재의 mid값ㅇ르 이용해 공유기 설치
    for i in range(1, n): # 앞에서부터 설치
        if nums[i] >= value + mid:
            value = nums[i]
            count += 1
    if count >= c : #C개 이상 공유기를 설치할 수 있는 겨우, 거리를 증가
        start = mid + 1
        result = mid # 최적의 결과를 저장
    else:       # c개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소
        end = mid - 1
        
print(result)
    