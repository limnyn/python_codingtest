# https://www.acmicpc.net/problem/19942
"""
[문제]
조건을 만족시키면서 가장 비용이 적은 경우

[제약]
3 <= N <= 15

[접근]
N이 최대 15, 모든 부분집합의 경우의 수는 2^15
따라서 완전 탐색으로 최소값을 찾을 수 있다.
"""
import sys, itertools
def input(): return sys.stdin.readline().rstrip()

def calc_nutrient(arr):
    global result, result_group
    cost, nutrient_sum = 0, [0] * 4
    for food_num in arr:
        for i in range(4):
            nutrient_sum[i] += ingredient[food_num][i]
        cost += ingredient[food_num][4]
    
    if cost > result:
            return False
    else:
        for i in range(4):
            if min_reference[i] > nutrient_sum[i]:
                return False
        
        if cost == result:
            result_group.append(arr)
        else:
            result_group = [arr]
            result = cost
        return True
    
if __name__ == "__main__":
    n = int(input())
    min_reference = list(map(int, input().split()))
    
    ingredient = []
    for i in range(n):
        ingredient.append(list(map(int, input().split())))
    
    
    result = float("inf")
    result_group = []
    
    foods = list(range(n))
    for i in range(n):
        combs = itertools.combinations(foods, i + 1)
        for comb in combs:
            calc_nutrient(comb)

    if result == float("inf"):
        print(-1)
    else:
        print(result)
        result_group.sort()
        for x in result_group[0]: 
            print(x + 1, end = " ") 






    
    
