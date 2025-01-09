# https://www.acmicpc.net/problem/1744
"""
접근
1 .정렬
2. (음수 및 0), (양수) 두 수열로 나눈다
3. 음수는 가장 작은 수 부터 두 쌍씩 그룹짓고 없으면 더한다
4. 양수는 가장 큰 수부터 두 쌍씩 그룹짓고 숫자가 1이거나 쌍이 없으면 더한다

"""
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

if __name__ == "__main__":
    
    n = int(input())
    arr = []
    
    for _ in range(n):
        arr.append(int(input()))
    arr.sort()
    
    negative = [x for x in arr if x <= 0]
    postive = [x for x in arr if x > 0]



    result = 0

    neg_dq = deque(negative)
    while neg_dq:
        a = neg_dq.popleft()
        if neg_dq:
            b = neg_dq.popleft()
            result += a * b
        else:
            result += a
    
    pos_dq = deque(postive)
    while pos_dq:
        a = pos_dq.pop()
        
        # 1은 곱하지 않고 더한다
        if a == 1:
            result += 1
            continue

        if pos_dq:
            b = pos_dq.pop()
            if b == 1: # 1은 곱하지 않고 더한다
                result += a + b
            else:
                result += a * b
        else:
            result += a

    print(result)    
    
        

        



