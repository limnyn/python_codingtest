# 입력 조건
#     첫째 줄에 정수 N이 주어진다.
#     둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다.
#     이때 정수는 1보다 크고 1000000 이하이다.
#     셋째 줄에는 정수 M이 주어진다.
#     넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다. 이때 정수는 1보다 크고  10억 이하이다.

# 출력 조건
#     첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes를, 없으면 no를 출력한다.


# 입력 예시
#     5
#     8 3 7 9 2
#     3
#     5 7 9

# 출력 예시
#     no yes yes




def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

stock = int(input())

array = list(map(int, input().split()))

array.sort()


m = int(input())
x = list(map(int, input().split()))

    
        

for i in x:
    # if o in items:
    result = binary_search(array, i,0,len(array)-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no',end=' ')

print()

