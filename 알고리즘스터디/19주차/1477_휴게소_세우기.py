# https://www.acmicpc.net/problem/1477
'''
[문제]
    주어진 상황에서 휴게소를 M개를 더 설치해서
    가장 가까운 휴게소 사이의 거리가 가장 긴 경우가 최소로 되도록 하기

[조건]
    0 ≤ N ≤ 50
    1 ≤ M ≤ 100
    100 ≤ L ≤ 1,000

[접근]
    1. 우선순위 큐를 사용해서 가장 긴 거리의 휴게소 사이에 휴게소를 설치하는 것을 반복한다.
        => 실패, 항상 두 휴게소 중앙에 휴게소를 설치한은것이 정답이 아닐 수 있음

    2. 파라매트릭 서치 응용
        -> 공유기 설치 문제처럼 접근

        1. 두 휴게소 사이의 최소 거리를 dist 라고 할 때, 
            만약  m개를 놓아서 dist인 거리를 유지할 수 있는지 확인한다.
        2-1. 만약 m개를 놓아서 dist인 거리를 유지할 수 없다면 dist를 늘린다
        2-2. 만약 m개를 놓아서 dist인 거리를 유지할 수 있다면 dist를 줄인다
'''
import sys, heapq
def input(): return sys.stdin.readline().rstrip()



def can_install(mid, existing_stops, new_stops):
    count = 0
    for i in range(1, len(existing_stops)):
        distance = existing_stops[i] - existing_stops[i - 1]
        if distance > mid:
            count += (distance - 1) // mid
    return count <= new_stops

def find_min_max_distance(existing_stops, new_stops, highway_length):
    existing_stops.sort()
    
    left, right = 1, highway_length
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        if can_install(mid, existing_stops, new_stops):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer



if __name__ == "__main__":
    n, new_stops, highway_length = map(int, input().split())
    existing_stops = sorted([0] + list(map(int, input().split())) + [highway_length]) #휴게소 입력 후 정렬
    
    result = find_min_max_distance(existing_stops, new_stops, highway_length)
    
    print(result)  


