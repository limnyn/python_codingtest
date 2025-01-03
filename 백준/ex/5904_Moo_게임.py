# https://www.acmicpc.net/problem/5904

'''
[접근]
1. K가 주어졌을 때 S(K-1), (K+3), S(K-1) 세 가지 구역으로 나눈다,
2. K가 세 가지 구역 중 어디에 포함되는지 확인한다.
3. K - 포함되는 구역의 시작점 인덱스를 사용해서 계산한다.
    3-1
        1, 3번째 구역인 (K - 해당 구역 시작 인덱스)를 계산해서
        S(K-1)에서의 위치를 계산한다. 그리고 1번부터 반복한다.
    3-2
        2번째 구역인 경우
        K가 2번 구역 시작 인덱스인 경우 m, 이외에 o를 반환한다.

[필요한 모듈]
K 가 주어졌을 때 길이를 구하는 모듈
'''
import sys
def input(): return sys.stdin.readline().rstrip()

memo = {}
def find_length(k):
    """S(K)의 길이를 계산, (log N 시간복잡도)"""
    if k == 0:
        return 3
    if k in memo:
        return memo[k]  # 이미 계산된 값이 있으면 그대로 반환
    # 계산 후 메모에 저장
    memo[k] = 2 * find_length(k - 1) + (k + 3)
    return memo[k]

def solve(n, k):
    '''
    이후 해당 S(K)에서의 세 구역에 대한 시작 인덱스를 구한다
    가운데 구역인 경우 바로 답을 계산해서 반환한다.
    가운데 구역이 아닌 경우 recursion(k-1,(현재인덱스 - 구역 시작 인덱스))를 반복한다.
    만약 S(0)에 도달할 경우 값을 반환한다
    '''

    if k == 0:
        # S(0)인 경우
        return "m" if n == 1 else "o"
    
    length_k_minus_1 = find_length(k - 1)
    middle_length = k + 3

    if n <= length_k_minus_1:
        return solve(n, k-1)
    elif n <= length_k_minus_1 + middle_length:
        return "m" if n == length_k_minus_1 + 1 else "o"
    else:
        return solve(n - length_k_minus_1 - middle_length, k - 1)
    
def find_moo(n):
    k = 0
    while find_length(k) < n:
        k += 1
    return solve(n, k)


if __name__ == "__main__":
    n = int(input())
    print(find_moo(n))