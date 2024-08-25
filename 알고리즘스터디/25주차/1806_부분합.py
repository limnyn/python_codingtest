# https://www.acmicpc.net/problem/1806
'''
10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다.
이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상 되는 것 중
가장 짧은 것의 길이를 구하는 프로그램

[입력]
10 <= N <= 100,000
0 <= S <= 100,000,000

[출력]
구하고자 하는 최소 길이를 출력.
합을 만드는 것이 불가능하면 0을 출력

[접근 - 투포인터]
start, end 두개의 포인터를 통해
start, end = 0, 0
S 이상이 될 때 까지
end를 증가시키고
S 이상이 되면 길이를 갱신
그리고 start<end일 때 까지 start+=1
start == end 이면 다시 
end += 1 해 나 간다.
'''
import sys
def input(): return sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    left, right = 0, 0
    min_len = float('inf')
    partition_sum = 0
    
    while True:
        if partition_sum >= s:
            min_len = min(min_len, right - left)
            partition_sum -= arr[left]
            left += 1
        elif right == n:
            break
        else:
            partition_sum += arr[right]
            right += 1
    
    if min_len == float('inf'):
        print(0)
    else:
        print(min_len)
        
        
        
        



