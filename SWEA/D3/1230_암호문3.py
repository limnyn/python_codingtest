for t in range(1, 11):
    cryptlen = int(input())

    nums = list(map(int, input().split()))

    opers_len = int(input())
    opers_str = list(input().split())
    opers = []
    for i, o in enumerate(opers_str):
        if o == "I":
            x, y = int(opers_str[i + 1]), int(opers_str[i + 2])
            s = list(map(int, opers_str[i + 3 : i + 3 + y]))
            opers.append([o, x, y] + s)
        elif o == "D":
            x, y = int(opers_str[i + 1]), int(opers_str[i + 2])
            opers.append([o, x, y])
        elif o == "A":
            x, y = -1, int(opers_str[i + 1])
            s = list(map(int, opers_str[i + 2 : i + 2 + y]))
            opers.append([o, x, y, s])

    for oper in opers:
        o, x, y = oper[0], oper[1], oper[2]
        if o == "I":
            nums[x:x] = oper[3:]
        elif o == "D":
            nums[x : x + y] = []
        elif o == "A":
            nums += oper[3:]

    print(f"#{t}", end=" ")
    for num in nums[:10]:
        print(num, end=" ")
    print()
