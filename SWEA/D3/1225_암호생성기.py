from collections import deque

for t in range(1, 11):
    T = int(input())

    nums = deque(list(map(int, input().split())))
    end = False
    while end == False:
        for i in range(1, 6):
            a = nums.popleft() - i
            if a <= 0:
                a = 0
                nums.append(a)
                end = True
                break
            nums.append(a)
    print(f"#{T}", end=" ")
    for num in nums:
        print(num, end=" ")
    print()
