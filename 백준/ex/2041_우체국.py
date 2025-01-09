# https://acmicpc.net/problem/2141
"""
[문제]
일직선 상의 각 마을에서 사람들이 살고 있다.
이 때 각 "사람"들까지의 거리의 합이 최소가 되는 위치에 우체국을 세우려 한다
특정 좌표(우체국) 구하기

[제약]
1 <= N <= 100,000
|X[i]| <= 1,000,000,000
1 <= |A[i]| <= 1,000,000,000
모든 입력은 정수

[출력]
우체국의 좌표를 출력한다.
만약 가능한 경우가 여러가지 인 경우에는 더 작은 위치를 출력하도록 한다.

[접근]
"가중치가 있는 중앙값 찾기"

1. 마을을 번호별로 정렬한다
2. 0번 마을에서부터 해당 마을 기준 왼쪽과 오른쪽에 총 인구가 몇명있는지 계산한다.
3. 누적 인구가 전체 인구의 절반 이상이 되는 첫 번째 위치를 찾는다.
4. 해당 위치가 우체국을 지을 최적의 위치

이동 거리 계산
    한 위치를 기준으로 이동 거리의 총합을 계산하면, 좌우로 더 멀리 있는 점에서 발생하는 거리 차이가 증가하기 때문에, 중앙값이 최소 거리의 합을 보장한다.

"""
import sys
def input(): return sys.stdin.readline().rstrip()

if __name__ == "__main__":
    
    n = int(input())
    
    arr = []
    population_sum = 0
    for _ in range(n):
        
        viliage_num, population = map(int, input().split())
        population_sum += population

        arr.append((viliage_num, population))
    


    arr.sort(key= lambda x: x[0])
    
    half_population = population_sum / 2
    left_population = 0
    
    for i in range(n):
        
        viliage_num, population = arr[i]
        left_population += population

        if left_population >= half_population:
            print(viliage_num)
            break

        
        


