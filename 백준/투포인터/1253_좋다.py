# https://www.acmicpc.net/problem/1253

'''
N개의 수 중에서 어떤 수가 다른 수 두개의 합으로 나타낼 수 있는지
해당 경우의 수를 출력하는 문제

[입력]
1 <= N <= 2000

[접근]
투 포인터로 풀기
'''

import sys
def input(): return sys.stdin.readline().rstrip()

if __name__ == "__main__":
    # 입력
    N = int(input())
    nums = sorted(list(map(int, input().split())))
    
    good_cnt = 0

    if N == 1:
        print(0)
        exit()
            

    for i in range(N):
        target = nums[i]
        left, right = 0, N - 1

        while left < right:
            
            if left == i:
                left += 1
                continue
            
            if right == i:
                right -= 1
                continue

            sum_num = nums[left] + nums[right]
            if target == sum_num:
                good_cnt += 1
                break
            elif sum_num < target:
                left += 1
            elif sum_num > target:
                right -= 1

    print(good_cnt)



'''
[후기]
문제가 설명과 테스트케이스가 너무 부실해서 이해하기 어려웠다
5
-1 0 1 2 3
이 테스트케이스를 보고 문제를 이해할 수 있었다.
'''