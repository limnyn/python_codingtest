for t in range(1, 11):
    cryptlen = int(input())

    nums = list(map(int, input().split()))
    opers_len = int(input())
    opers = list(input().split("I"))

    opers = [list(map(int, x.split())) for x in opers[1:]]

    for oper in opers:
        x, y = oper[0], oper[1]

        nums[x:x] = oper[2:]

    print(f"#{t}", end=" ")
    for num in nums[:10]:
        print(num, end=" ")
    print()
