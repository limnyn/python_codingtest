# https://www.acmicpc.net/problem/12920


'''
산다 안산다 2진수
    비용이 A인 특정 물건이 5개 있을때 사는 경우
        000 ~ 100
        2진수 3비트로 물건을 사는 수를 포함 가능하다
        따라서 비용이 A, A*2, A*3인 아이템이 있는 경우와 동일하다.
        그러므로 c개 있을때는 물건을 c보다 작은 2진수 갯수로 구한다
        
        ex) c가 5면 3 c가 15면 4

        
    비용이 3인 물체 5개
    
    5개
    -> 행 + 5

    5 -> 101
    2^3 2^1

    
    해당 계산을 하기 위해서는?
    
    1 <= C <= 10000
    
    2^14를 넘지 않는다,
    
    for문을 통해 갯수 c를 표현 가능하도록 해당 수의 2진수 변환 시 자리 수 만큼
    물건을 해당 진수의 배수만큼 더 추가해준다.


    메모리 초과를 막기 위해
        5개인 경우 1, 2, 2개인 경우를 추가해준다

'''
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

w = []
v = []
for _ in range(n):
    weight, value, count = map(int,input().split())
    
    bit_len = 0
    sum_bit = 0 
    while True:
        sum_bit += 2**bit_len
        if sum_bit <= count:
            w.append(weight*2**bit_len)
            v.append(value*2**bit_len)
            bit_len += 1
        else:
            if count - (sum_bit - 2 ** bit_len) != 0:
                w.append(weight*(count-(sum_bit-2**bit_len)))
                v.append(value*(count-(sum_bit-2**bit_len)))
            break             



dp = [[0] * (m+1) for _ in range(len(w)+1)]
bf_dp = [0] * (m+1)
for r in range(1, len(w)+1):
    af_dp = [0]*(m+1)
    for c in range(1, m+1):
        if c-w[r-1] >= 0:
            af_dp[c] = max(bf_dp[c], bf_dp[c-w[r-1]]+v[r-1])
        else:
            af_dp[c] = bf_dp[c]
    bf_dp = af_dp

    

print(af_dp[-1])
