# https://www.acmicpc.net/problem/14921
"""
정렬 후 투 포인터로 접근하기
"""
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    arr = sorted(list(map(int, input().split())))

    result = float("inf")
    left, right = 0, len(arr) - 1
    while left < right:
        compound = arr[left] + arr[right]
        
        if compound < 0:
            left += 1
        elif compound > 0:
            right -= 1
        else:
            result = 0
            break

        if abs(compound) < abs(result): 
            result = compound
    
    print(result)


        

if __name__ == "__main__":
    main()