# https://www.acmicpc.net/problem/7453

'''
[문제]
    4개를 선택했을 때 0이 되는 쌍의 갯수

[입력]
    1 <= n <= 4000
    n개의 줄에는 4개의 숫자가 주어진다.
    각 정수의 절대값 <= 2^28

[접근]
    [1. 모든 경우를 탐색한다면?]
        최악의 경우 4000C4 -> 10,650,673,999,000
        -> 시간 초과
    [2. 두 수 a, b를 찾고, a+b와 동일한 c+b 쌍을 찾으면?]
        4000c2 * 4000 -> 7,998,000 * 4000
        -> 시간 초과
    [3. A[a], B[b] 조합의 합을 map에 저장하고 해당값과 합이 0이되는 C, D 찾기]
        
        if dict[-1*(C[c] + D[d])]:
            result += dict[-1*( C[C] + D[d] )]

        A[a] + B[b] 쌍
            4000*4000 -> 16,000,000
        C[c] + D[d] 쌍
            16,000,000
            -> 32,000,000번 언에 연산 가능       
        
    성공!
'''

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    A, B, C, D = [], [], [], []
    for _ in range(n):
        a, b, c, d = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)

    result = 0
    dict_AB = {}
    for a in range(n):
        for b in range(n):
            if A[a]+B[b] in dict_AB:
                dict_AB[A[a]+B[b]] += 1
            else:
                dict_AB[A[a]+B[b]] = 1
    
    for c in range(n):
        for d in range(n):
            if -(C[c]+D[d]) in dict_AB:
                result += dict_AB[-(C[c]+D[d])]
    
    print(result)

