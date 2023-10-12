T = int(input())

for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    y = ""
    if a < b:
        y = "<"
    elif a == b:
        y = "="
    else:
        y = ">"

    print("#" + str(test_case) + " " + y)
