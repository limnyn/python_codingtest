T = int(input())


for test_case in range(1, T + 1):
    nums = list(map(int, input().split()))
    result = round(sum(nums) / len(nums))
    print("#" + str(test_case) + " " + str(result))
