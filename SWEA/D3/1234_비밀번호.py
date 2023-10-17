for t in range(1, 11):
    num_len, nums = input().split()
    num_len = int(num_len)
    nums = [int(x) for x in nums]

    no_more_same = False
    while no_more_same == False:
        for i in range(len(nums)):
            if i == len(nums) - 1:
                no_more_same = True
                break
            if nums[i] == nums[i + 1]:
                nums[i : i + 2] = []
                break

    result = ""
    for n in nums:
        result += str(n)
    print(f"#{t} {result}")
