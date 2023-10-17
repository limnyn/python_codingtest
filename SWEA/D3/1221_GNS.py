nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())
for t in range(1, T + 1):
    testcase, n = input().split()
    n = int(n)

    line = list(input().split())
    result = []
    for num in line:
        result.append(nums.index(num))

    result.sort()
    answer = [nums[x] for x in result]
    print(testcase)
    for ans in answer:
        print(ans, end=" ")
    print()
