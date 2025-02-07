# https://www.acmicpc.net/problem/22945
"""
투포인터
"""
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    left, right = 0, n - 1

    result = 0
    while left < right:
        a, b = arr[left], arr[right]
        
        result = max(result, (right - left - 1) * min(a, b))

        if a <= b:
            left += 1
        else:
            right -= 1
    print(result)


if __name__ == "__main__":
    main()